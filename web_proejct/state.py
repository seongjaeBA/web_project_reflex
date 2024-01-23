import os
import re
import pickle
import json
from typing import List, Any
from dotenv import load_dotenv 
from datetime import datetime, timezone


import reflex as rx
from web_proejct.model import Movie
from web_proejct.crawapi import add_rank

import httpx
import asyncio
import requests
from sqlmodel import select

import pandas as pd

import openai
import torch
from openai import OpenAI

import tiktoken
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from bigdl.llm.transformers import AutoModelForCausalLM


load_dotenv(dotenv_path='../env/.env')
openai.api_key = os.environ["OPENAI_API_KEY"]
KMDB_API = os.environ["KMDB_API"]

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")


# def get_llama_prompt(message: str, chat_history: list[tuple[str, str]],
#                system_prompt: str) -> str:
#     texts = [f'<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n']
#     # The first user input is _not_ stripped
#     do_strip = False
#     for user_input, response in chat_history:
#         user_input = user_input.strip() if do_strip else user_input
#         do_strip = True
#         texts.append(f'{user_input} [/INST] {response.strip()} </s><s>[INST] ')
#     message = message.strip() if do_strip else message
#     texts.append(f'{message} [/INST]')
#     return ''.join(texts)


class chatQA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


DEFAULT_CHATS = {
    "Intros": [],
}


class chatState(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[chatQA]] = DEFAULT_CHATS

    # The current chat name.
    current_chat = "Intros"

    # The current question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""

    # Whether the drawer is open.
    drawer_open: bool = False

    # Whether the modal is open.
    modal_open: bool = False

    api_type: str = "openai"

    def create_chat(self):
        """Create a new chat."""
        # Add the new chat to the list of chats.
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

        # Toggle the modal.
        self.modal_open = False

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]
        self.toggle_drawer()

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name
        self.toggle_drawer()

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        # Get the question from the form
        question = form_data["question"]

        # Check if the question is empty
        if question == "":
            return

        model = self.openai_process_question

        async for value in model(question):
            yield value

    async def openai_process_question(self, question: str):
        """Get the response from the API.

        Args:
            form_data: A dict with the current question.
        """

        # Add the question to the list of questions.
        qa = chatQA(question=question, answer="")
        self.chats[self.current_chat].append(qa)

        # Clear the input and start the processing.
        self.processing = True
        yield

        # Build the messages to GPT.
        messages = [
            {"role": "system", "content": "You are a movie scenario writer named Cinebot."}
        ]
        
        
        for qa in self.chats[self.current_chat]:
            messages.append({"role": "user", "content": qa.question})
            messages.append({"role": "assistant", "content": qa.answer})
            
        # Build the messages to GPT.

        # Remove the last mock answer.
        messages = messages[:-1]

        # new session with llama
        get_llama_prompt(qa, self.chats[self.current_chat], messages)
        model = AutoModelForCausalLM.from_pretrained(
            model_path = "meta-llama/Llama-2-7b-chat-hf",
            load_in_low_bit="nf4",
            optimize_model=True,
            trust_remote_code=True,
            use_cache=True,
            torch_dtype=torch.bfloat16,
            modules_to_not_convert=["lm_head"],
            )
        model = model.to('xpu')
        
        
        # Start a new session to answer the question.
        session = openai.ChatCompletion.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=messages,
            stream=True,
        )

        # Stream the results, yielding after every word.
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer_text = item.choices[0].delta.content
                self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield

        # Toggle the processing flag.
        self.processing = False



# "-------------------------------------------------------------------------------------"
def normalize_text(s, sep_token = " \n "):
    s = re.sub(r'\s+',  ' ', s).strip()
    s = re.sub(r". ,","",s)
    # remove all instances of multiple spaces
    s = s.replace("..",".")
    s = s.replace(". .",".")
    s = s.replace("\n", "")
    s = s.replace("#","")
    s = s.strip()
    if s =="":
        s = "<blank>"
        
    return s


class lanchainState(rx.State):

    # The current large text to be summarized.
    large_text: str
    # openai key
    openai_api_key: str = openai.api_key
    # the result
    summary: str
    is_loading: bool = False
    loading_text: str = ""

    def start_process(self):
        self.is_loading = True
        self.loading_text = "문서 요약중...."

        return lanchainState.summarize

    def summarize(self):
        model_name = "gpt-3.5-turbo-16k"
        llm = ChatOpenAI(
                        temperature=0, 
                        model_name= model_name, 
                        streaming=True, 
                        openai_api_key=self.openai_api_key
                        )
        large_text = self.large_text
        nom_text = normalize_text(large_text)
        tokenizer = tiktoken.get_encoding("cl100k_base")
        # tok = nom_text.copy()
        # tok['n_tokens'] = nom_text["CONTENT"].apply(lambda x: len(tokenizer.encode(x)))
        # print(tok)
        # print(len(tok))
        
        docs = [Document(page_content=t) for t in nom_text]
        # print(len(docs))
        
        # use load_summarize_chain to summarize the full text and return self.summary to frontend
        chain = load_summarize_chain(llm, chain_type="stuff")
        try:
            self.summary = chain.invoke(docs)
        except Exception as error:
            print("에러 발생",error)
            self.summary = '실패'
        finally:
            self.summary
        yield

        # reset state variable again
        self.is_loading = False
        self.loading_text = ""
        

# class MovieState(rx.State):
#     movie_dict: dict = pickle.load(open("../env/movie_dict.pkl", "rb"))
#     movies: list = list(movie_dict["title"].values())
#     show: bool = False
#     selected_movie: str
#     recommended_movies: list = []
#     recommended_movies_poster: list = []
#     recommendation: list = []

#     def fetch_poster(self, movie_id):
#         response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, os.environ['TMDB_KEY']))
#         data = response.json()
#         poster_url = 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
#         return poster_url

#     def predict(self):
#         self.recommended_movies = []
#         self.recommended_movies_poster = []

#         similarity = pickle.load(open('../env/similarity.pkl', 'rb'))

#         movies = pd.DataFrame(self.movie_dict)
#         movie_index = movies[movies['title'] == self.selected_movie].index[0]
#         distance = similarity[movie_index]
#         movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:7]

        
#         for i in movies_list:
#             movie_id = movies.iloc[i[0]].movie_id
#             self.recommended_movies.append(movies.iloc[i[0]].title)
#             poster_url = self.fetch_poster(movie_id)
#             self.recommended_movies_poster.append(poster_url)

#         self.show = True


client = OpenAI()


class daleState(rx.State):
    """The app state."""

    image_url = ""
    image_processing = False
    image_made = False

    def get_dalle_result(self, form_data: dict[str, str]):
        prompt_text: str = form_data["prompt_text"]
        self.image_made = False
        self.image_processing = True
        yield
        try:
            response = client.images.generate(prompt=prompt_text, n=1, size="1024x1024")
            self.image_url = response.data[0].url
            self.image_processing = False
            self.image_made = True
            yield
        except Exception as e:
            print(e)
            self.image_processing = False
            yield rx.window_alert("Error with OpenAI Execution.")


# "----------------------------------------------------------"


class openState(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a movie director, skilled in writing creative movie scenario."},
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )
        
        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield
                
                


# UploadState----------------------------------------------

class UploadState(rx.State):
    """The app state."""

    # Whether we are currently uploading files.
    is_uploading: bool

    @rx.var
    def file_str(self) -> str:
        """Get the string representation of the uploaded files."""
        return "\n".join(os.listdir(rx.get_asset_path()))

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the file upload."""
        self.is_uploading = True

        # Iterate through the uploaded files.
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

        # Stop the upload.
        return UploadState.stop_upload

    async def stop_upload(self):
        """Stop the file upload."""
        await asyncio.sleep(1)
        self.is_uploading = False
        
        
# CRUD ------------------------------------------------------------------

DEFAULT_BODY = """{
    "MovieCode":"",
    "Title":"",
    "image":"/favicon.ico",
    "Year": 0,
    "Genre":"",
    "Director":"",
    "Actors":""
}"""

URL_OPTIONS = {
    "검색": "Movie",
    "쓰기": "Movie",
    "수정": "Movie/{pr_id}",
    "삭제": "Movie/{pr_id}",
}


class CRUDState(rx.State):
    """The app state."""
    code: str
    movies: list[Movie]
    _db_updated: bool = False
    
    def load_movie(self):
        with rx.session() as session:
            self.movies = session.exec(select(Movie)).all()
        yield CRUDState.reload_movie

    @rx.background
    async def reload_movie(self):
        while True:
            await asyncio.sleep(2)
            if self.db_updated:
                async with self:
                    with rx.session() as session:
                        self.movies = session.exec(select(Movie)).all()
                    self._db_updated = False

    @rx.var
    def db_updated(self):
        return self._db_updated

    @rx.var
    def total(self):
        return len(self.movies)


class QueryState(CRUDState):
    body: str = DEFAULT_BODY
    response_code: str = ""
    response: str = ""
    method: str = "GET"
    url_query: str = URL_OPTIONS["검색"]
    query_options = list(URL_OPTIONS.keys())

    def update_method(self, value):
        if self.url_query == "":
            self.url_query = URL_OPTIONS[value]
        self.method = value

    @rx.var
    def need_body(self):
        return False

    @rx.var
    def f_response(self):
        return f"""```json\n{self.response}\n```"""

    def clear_query(self):
        self.url_query = URL_OPTIONS["검색"]
        self.method = "GET"
        self.body = DEFAULT_BODY

    async def send_query(self):
        url = f"http://localhost:8000/{self.url_query}"
        async with httpx.AsyncClient() as client:
            match self.method:
                case "GET":
                    res = await client.get(url)
                case "POST":
                    res = await client.post(url, data=self.body)
                case "PUT":
                    res = await client.put(url, data=self.body)
                case "DELETE":
                    res = await client.delete(url)
                case _:
                    res = None
        self.response_code = res.status_code
        if self.response_code == 200:
            self.response = json.dumps(res.json(), indent=2)
            self._db_updated = True
        else:
            self.response = res.content.decode()
            
            
            
#---------------------------table-------------------



class BaseState(rx.State):
    pass

class DataTableState(BaseState):
    """The app state."""

    clicked_cell: str = "Cell clicked: "
    edited_cell: str = "Cell edited: "
    right_clicked_group_header: str = "Group header right clicked: "
    item_hovered: str = "Item Hovered: "
    deleted: str = "Deleted: "
    table_data: list[dict[str, Any]] = []
    cral_data: dict[str, Any] = {}

    cols: list[dict[str, str]] = [
        {
            "title": "platform", 
            "type": "str",
            "width": 100,
        },
        {
            "title": "date", 
            "type": datetime,
            "width": 100,
        },
        {
            "title": "Rank1",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank2",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank3",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank4",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank5",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank6",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank7",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank8",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank9",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "Rank10",
            "type": "str",
            "group": "data",
            "width": 150,
        },
        {
            "title": "v1",
            "type": bool,
            "group": "check",
            "width": 50,
        },
    ]

    def set_dailyrank(self):
        data: dict[str, Any] = {}
        today: datetime.date = datetime.now(timezone.utc).date()
        data["rankdate"] = today.strftime("%Y-%m-%d")
        print(data["rankdate"])
        self.cral_data = add_rank(data)
        print(self.cral_data)
        for i in self.cral_data:
            print(i)
            if i == 'rankdate':
                continue
            self.table_data.append(
                {
                "platform": i,
                "date": today,
                "Rank1":self.cral_data[i]["Rank1"],
                "Rank2":self.cral_data[i]["Rank2"],
                "Rank3":self.cral_data[i]["Rank3"],
                "Rank4":self.cral_data[i]["Rank4"],
                "Rank5":self.cral_data[i]["Rank5"],
                "Rank6":self.cral_data[i]["Rank6"],
                "Rank7":self.cral_data[i]["Rank7"],
                "Rank8":self.cral_data[i]["Rank8"],
                "Rank9":self.cral_data[i]["Rank9"],
                "Rank10":self.cral_data[i]["Rank10"],
                "v1": False
            }
        )
        print(self.table_data)
        self.cral_data = {}

    def get_clicked_data(self, pos) -> str:
        self.clicked_cell = f"Cell clicked: {pos}"

    def get_edited_data(self, pos, val) -> str:
        col, row = pos
        self.data[row][col] = val["data"]
        self.edited_cell = f"Cell edited: {pos}, Cell value: {val['data']}"

    def get_group_header_right_click(self, index, val):
        self.right_clicked_group_header = f"Group header right clicked at index: {index}, Group header value: {val['group']}"

    def get_item_hovered(self, pos) -> str:
        self.item_hovered = (
            f"Item Hovered type: {pos['kind']}, Location: {pos['location']}"
        )

    def get_deleted_item(self, selection):
        self.deleted = f"Deleted cell: {selection['current']['cell']}"

    # def append_row(self):
    #     print("13232")

    def column_resize(self, col, width):
        self.cols[col["pos"]]["width"] = width


class KMDBTableLiveState(BaseState):
    keyword : str = ""
    response: str = ""
    table_data: list[dict[str, Any]] = []
    KMDB_API = KMDB_API
    columns: list[dict[str, str]] = [
        {
            "title": "movieId",
            "id": "v1",
            "type": "str",
            "width": 50,
        },
        {
            "title": "title",
            "id": "v2",
            "type": "str",
            "width": 200,
        },
        {
            "title": "directors",
            "id": "v3",
            "type": "str",
            "width": 100,
        },
        {
            "title": "actors",
            "id": "v4",
            "type": "str",
            "width": 100,
        },
        {
            "title": "plots",
            "id": "v5",
            "type": "str",
            "width": 400,
        },
        {
            "title": "keywords",
            "id": "v6",
            "type": "str",
            "width": 100,
        },
        {
            "title": "poster",
            "id": "v7",
            "type": "str",
            "width": 100,
        },
        {
            "title": "moviecode",
            "id": "v8",
            "type": int,
            "width": 50,
        },
        {
            "title": "check",
            "id": "v9",
            "type": bool,
            "width": 50,
        },
    ]

    # async def get_movieinfo(self):
    def get_movieinfo(self):
        # async with httpx.AsyncClient() as client:
            # res = await client.get("http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&query=" + self.keyword + "&ServiceKey=" + self.KMDB_API)
            res = httpx.get("http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&query=" + self.keyword + "&ServiceKey=" + self.KMDB_API).json()["Data"][0]["Result"]
            for i in range(len(res)):
                data = res[i]
                self.table_data.append(
                    {
                    "v1": data["movieId"], 
                    "v2": data["title"],
                    "v3": data["directors"]["director"][0]["directorNm"],
                    "v4": ",".join(actor['actorNm'] for actor in data["actors"]['actor']),
                    "v5": data["plots"]["plot"][0]["plotText"],
                    "v6": data["keywords"],
                    "v7": data["posters"].split("|")[0],
                    "v8": data["Codes"]["Code"][0]["CodeNo"],
                    "v9": False
                    }
                )

class DataTableLiveState(BaseState):
    running: bool
    table_data: list[dict[str, Any]] = []
    rate: int = 0.4
    columns: list[dict[str, str]] = [
        {
            "title": "Id",
            "id": "v1",
            "type": "int",
            "width": 100,
        },
        {
            "title": "Advice",
            "id": "v2",
            "type": "str",
            "width": 750,
        },
    ]

    @rx.background
    async def live_stream(self):
        while True:
            await asyncio.sleep(1 / self.rate)
            async with self:
                if not self.running:
                    break

                if len(self.table_data) > 50:
                    self.table_data.pop(0)
                res = httpx.get("https://api.adviceslip.com/advice")
                data = res.json()
                self.table_data.append(
                    {"v1": data["slip"]["id"], "v2": data["slip"]["advice"]}
                )

    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            return DataTableLiveState.live_stream