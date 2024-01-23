import reflex as rx

from web_proejct import styles
from web_proejct.state import chatState


def sidebar_chat(chat: str) -> rx.Component:
    """A sidebar chat item.

    Args:
        chat: The chat item.
    """
    return rx.hstack(
        rx.box(
            chat,
            on_click=lambda: chatState.set_chat(chat),
            style=styles.sidebar_style,
            color=styles.icon_color,
            flex="1",
        ),
        rx.box(
            rx.icon(
                tag="delete",
                style=styles.icon_style,
                on_click=chatState.delete_chat,
            ),
            style=styles.sidebar_style,
        ),
        color=styles.text_light_color,
        cursor="pointer",
    )


def newchat_sidebar() -> rx.Component:
    """The sidebar component."""
    return rx.drawer(
        rx.drawer_overlay(
            rx.drawer_content(
                rx.drawer_header(
                    rx.hstack(
                        rx.text("Chats"),
                        rx.icon(
                            tag="close",
                            on_click=chatState.toggle_drawer,
                            style=styles.icon_style,
                        ),
                    )
                ),
                rx.drawer_body(
                    rx.vstack(
                        rx.foreach(chatState.chat_titles, lambda chat: sidebar_chat(chat)),
                        align_items="stretch",
                    )
                ),
            ),
        ),
        placement="left",
        is_open=chatState.drawer_open,
    )
