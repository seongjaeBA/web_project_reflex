import reflex as rx

from web_proejct import styles
from web_proejct.components import chat, modal, newchat_sidebar
from web_proejct.state import chatState
from web_proejct.templates import template

@template(route="/chatapp", title="ChatApp")
def chatapp() -> rx.Component:
    """The main app."""
    return rx.vstack(
        chat.chat(),
        chat.action_bar(),
        newchat_sidebar(),
        modal(),
        bg=styles.bg_dark_color,
        color=styles.text_light_color,
        min_h="100vh",
        align_items="stretch",
        spacing="0",
    )
