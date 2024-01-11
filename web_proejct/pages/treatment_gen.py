import reflex as rx

from web_proejct import styles as style
from web_proejct.templates import template
import os
import openai
from dotenv import load_dotenv 

load_dotenv(dotenv_path='../env/.env')
openai.api_key = os.environ["OPENAI_API_KEY"]


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
                
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            openState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=openState.question,
            placeholder="Ask a question",
            on_change=openState.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=openState.answer,
            style=style.button_style,
        ),
    )

@template(route="/treatment-gen", title="Treatment Generate")
def treatment() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )