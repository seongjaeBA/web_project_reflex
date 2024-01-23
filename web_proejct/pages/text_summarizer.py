import reflex as rx

from web_proejct.templates import template
from web_proejct.state import lanchainState
import web_proejct.styles as style

def full_text() -> rx.Component:
    """return a vertical component of heading and text_area."""
    return rx.vstack(
        rx.heading("원문",style=style.topic_style),
        rx.text_area(
            value=lanchainState.large_text,
            placeholder="원문을 입력해 주세요.",
            on_change=lanchainState.set_large_text,
            style=style.textarea_style,
        ),
    )


# def openai_key_input() -> rx.Component:
#     """return a password component"""
#     return rx.password(
#             value=lanchainState.openai_api_key,
#             placeholder="Enter your openai key",
#             on_change=lanchainState.set_openai_api_key,
#             style=style.openai_input_style,
#     )


def submit_button() -> rx.Component:
    """return a button."""
    return rx. center( 
        rx.button(
        "시작",
        on_click=lanchainState.start_process,
        is_loading=lanchainState.is_loading,
        loading_text=lanchainState.loading_text,
        spinner_placement="start",
        style=style.submit_button_style,
        )
    )


def summary_output() -> rx.Component:
    """return summary."""
    return rx.vstack(
                rx.heading("요약",style=style.topic_style),
                rx.text_area(
                    value=lanchainState.summary,
                    style=style.summary_style,
            ),
            
    )
    #             rx.box(
    #                 rx.text(lanchainState.summary, text_align="center"),
    #                 style=style.summary_style,
    # )

@template(route="/summarizer", title="LLM 문서 요약")
def summarizer() -> rx.Component:
    """return a full_text, openai_key_input, submit_button, summary_output respectively."""
    return rx.container(
        full_text(),
        # openai_key_input(),
        rx.spacer(),
        submit_button(),
        summary_output(),
    )