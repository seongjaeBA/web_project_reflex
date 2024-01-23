import reflex as rx

from web_proejct import styles
from web_proejct.state import chatState

def navbar_header() -> rx.Component:
    return rx.hstack(
                rx.spacer(),        
                rx.icon(
                    tag="hamburger",
                    mr=4,
                    on_click=chatState.toggle_drawer,
                    cursor="pointer",
                ),
            )


def navbar_item(text: str, icon: str, url: str) -> rx.Component:
    """
    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == f"/{text.lower()}") | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        href=url,
        width="100%",
    )

def navbar():
    from reflex.page import get_decorated_pages

    return rx.grid(
        rx.hstack(
            navbar_header(),
            rx.hstack(
                *[
                navbar_item(
                    text=page.get("title", page["route"].strip("/").capitalize()),
                        icon=page.get("image", "/github.svg"),
                        url=page["route"],
                )
                for page in get_decorated_pages()
                ],
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            rx.hstack(
                
                rx.button(
                    "+ New chat",
                    bg=styles.accent_color,
                    px="4",
                    py="2",
                    h="auto",
                    on_click=chatState.toggle_modal,
                ),
                rx.menu(
                    rx.menu_button(
                        rx.avatar(name="User", size="md"),
                        rx.box(),
                    ),
                    rx.menu_list(
                        rx.menu_item("Help"),
                        rx.menu_divider(),
                        rx.menu_item("Settings"),
                    ),
                ),
                spacing="8",
            ),
            justify="space-between",
            min_width=styles.navbar_width,
            height="100%",
            position="sticky",
            top="0px",
            border_right=styles.border,
        ),
        bg=styles.bg_dark_color,
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="4",
        border_bottom=f"1px solid {styles.border_color}",
        position="sticky",
        top="0",
        z_index="100",
    )
