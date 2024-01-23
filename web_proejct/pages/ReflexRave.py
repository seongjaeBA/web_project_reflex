import reflex as rx
import web_proejct.styles as style
from web_proejct.state import MovieState
from web_proejct.templates import template

def movie_card() -> rx.Component:

    return rx.vstack(
        rx.hstack(
            rx.select(
                MovieState.movies,
                on_change=MovieState.set_selected_movie,
                value=MovieState.selected_movie,
                placeholder="Select a movie",
                style=style.select,
            ),
            rx.button(
                "RaveMatch",
                on_click=MovieState.predict,
                style={
                    **style.border,
                    **style.button,
                    "padding": "0.75em",
                }
            )
        ),
        rx.vstack(
            rx.hstack(
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[0],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[0],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[1],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[1],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
            ),
            rx.hstack(
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[2],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[2],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[3],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[3],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
            ),
            rx.hstack(
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[4],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[4],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
                rx.card(
                    rx.image(
                        src=MovieState.recommended_movies_poster[5],
                        style=style.image,
                    ),
                    header=rx.heading(
                        MovieState.recommended_movies[5],
                        style=style.heading,    
                    ),
                    style={
                        **style.border,
                        **style.card,
                        "color":rx.cond(rx.color_mode == "light", "black", "white"),
                        "border_color": rx.cond(rx.color_mode == "light", "black", "white"),
                    },
                ),
            ),
            style={
                #make visible only when show is true
                "display": rx.cond(MovieState.show, "block", "none"),
            }
        ),

    )

@template(route="/TMDB_RAVE", title="TMDB RAVE")
def TMDB_RAVE() -> rx.Component:
    MovieState()

    return rx.container(
        rx.box(
            rx.heading("TMDB_Rave"),
            rx.text("유사 영화 추천"),
            style=style.hero_banner_text,            
        ),
        movie_card(),
        style=style.index,
        center_content=True,
    )