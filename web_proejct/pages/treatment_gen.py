import reflex as rx

import web_proejct.styles as style
from web_proejct.templates import template
from web_proejct.state import openState
                
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

@template(route="/treatment-gen", title="트리트먼트 도우미")
def treatment() -> rx.Component:
    return rx.vstack(
        rx.container(
        chat(),
        action_bar(),
        )
    )