"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from web_proejct.templates import template
from web_proejct.model import Movie
from web_proejct.state import CRUDState, QueryState
from typing import List

color = "rgb(107,99,246)"

def data_display():
    return rx.vstack(
        rx.heading(CRUDState.total, " : Movie found"),
        rx.foreach(CRUDState.movies, render_product),
        rx.spacer(),
        width="30vw",
        height="100vh",
        bg = "white"
    )


def render_product(movie: Movie):
    return rx.aspect_ratio(
        rx.hstack(
            rx.image(src=movie.image, 
                    #  height="100%", 
                     width="3vw"),
            rx.text(f"({movie.MovieCode}) {movie.Title}", width="10vw", color = color),
            rx.vstack(
                rx.text("Year:", movie.Year, color = color),
                rx.text("Genre:", movie.Genre, color = color),
                spacing="0",
                width="7vw",
            ),
            rx.vstack(
                rx.text("Director:", movie.Director, color = color),
                rx.text("Actors:", movie.Actors, color = color),
                spacing="0",
                width="7vw",
            ),
            rx.spacer(),
            border="solid black 1px",
            spcaing="5",
            width="100%",
        ),
    )

options: List[int] = list(range(1800, 2028))

class SelectState(rx.State):
    option: int = ""
    
class FormState(rx.State):
    form_data: dict = QueryState.body

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        QueryState.set_body = self.form_data
        
    
def query_form():
    return rx.vstack(
        rx.hstack(
            rx.text("검색 조건:"),
            rx.select(
                ["GET", "POST", "PUT", "DELETE"],
                on_change=QueryState.update_method,
            ),
            rx.input(
                value=QueryState.url_query,
                on_change=QueryState.set_url_query,
                width="30vw",
            ),
        ),
        
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Movie Code",
                    name = "MovieCode",
                ),
                rx.input(
                    placeholder="제목",
                    name = "Title",
                ),
                rx.input(
                    placeholder="image",
                    name = "image",
                ),
                rx.select(
                    options,
                    placeholder="개봉년도",
                    on_change=SelectState.set_option,
                    color_schemes = "black",
                    name = "Year",
                ),
                rx.input(
                    placeholder="장르",
                    name = "Genre",
                ),
                rx.input(
                    placeholder="감독",
                    name = "Director",
                ),
                rx.input(
                    placeholder="배우",
                    name = "Actors",
                    type_= "submit"
                ),
                rx.hstack(
                    rx.button("Clear", on_click=QueryState.clear_query),
                    rx.button("Send", on_click=QueryState.send_query),
                ),
            ),    
            on_submit= FormState.handle_submit,
            reset_on_submit= True
        ),
        # rx.text("내용:"),
        # rx.text_area(
        #     value=QueryState.body, height="30vh", on_change=QueryState.set_body
        # ),
        # rx.hstack(
        #     rx.button("Clear", on_click=QueryState.clear_query),
        #     rx.button("Send", on_click=QueryState.send_query),
        # ),
        rx.divider(orientation="horizontal", border="solid black 1px", width="100%"),
        rx.hstack(
            rx.text("Status: ", QueryState.response_code), rx.spacer(), width="100%"
        ),
        rx.container(
            rx.text(FormState.form_data.to_string()),
        ),
        rx.container(
            rx.markdown(
                QueryState.f_response,
                language="json",
                height="30vh",
            )
        ),
        width="50vw",
        # width="100%",
    )

@template(route="/", title="무비 인풋",on_load=CRUDState.load_movie)
def index() -> rx.Component:
    return rx.hstack(
        # rx.spacer(),
        data_display(),
        rx.spacer(),
        rx.divider(orientation="vertical", border="solid black 1px"),
        query_form(),
        rx.spacer(),
        height="100%",
        width="100vw",
        spacing="0",
    )
