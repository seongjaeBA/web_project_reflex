from web_proejct.templates import template
from web_proejct.state import daleState
from web_proejct import styles

import reflex as rx

@template(route="/Dalle", title="이미지 생성")
def dalle():
    return rx.container(
        rx.vstack(
            rx.heading("DALL-E", font_size="1.5em"),
            rx.form(
                rx.input(id="prompt_text", placeholder="Enter a prompt.."),
                rx.button(
                    "Generate Image",
                    type_="submit",
                    width="100%",
                    color_scheme= 'blackAlpha',
                    bg=styles.accent_color,
                ),
                on_submit=daleState.get_dalle_result,
            ),
            rx.divider(),
            rx.cond(
                daleState.image_processing,
                rx.circular_progress(is_indeterminate=True),
                rx.cond(
                    daleState.image_made,
                    rx.image(
                        src=daleState.image_url,
                        height="25em",
                        width="25em",
                    ),
                ),
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
            width="100%",
            height="100vh",
            # background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )