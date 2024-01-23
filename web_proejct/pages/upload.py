from web_proejct.state import UploadState
from web_proejct.templates import template

import reflex as rx

color = "rgb(107,99,246)"

@template(route="/upload", title="파일 업로드 to me")
def upload() -> rx.component:
    return rx.vstack(
        rx.center(
            rx.upload(
                rx.button(
                    "Select File(s)",
                    height="70px",
                    width="200px",
                    color=color,
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files",
                    height="100px",
                    width="200px",
                ),
                border="1px dotted black",
                padding="2em",
            ),
        ),
        rx.center(
            rx.button(
                "Upload",
                color=color,
                on_click=UploadState.handle_upload(rx.upload_files()),
            ),
        ),
        rx.heading("Files:", color = color),
        rx.cond(
            UploadState.is_uploading,
            rx.progress(is_indeterminate=True, color="blue", width="100%"),
            rx.progress(value=0, width="100%"),
        ),
        rx.text_area(
            is_disabled=True,
            value=UploadState.file_str,
            width="100%",
            height="100%",
            bg="white",
            color="black",
            placeholder="No File",
            min_height="20em",
        ),
    )

