"""Styles for the app."""

import reflex as rx

bg_dark_color = "#111"
bg_medium_color = "#222"

border_color = "#fff3"
border_radius = "0.375rem"
border = "1px solid #F4F3F6"

accennt_light = "#6649D8"
accent_color = "#5535d4"
accent_dark = "#4c2db3"
accent_text_color = "#1A1060"
btn_accent_color = "#F5EFFE"
hover_accent_color = {"_hover": {"color": btn_accent_color}}
hover_accent_bg = {"_hover": {"bg": btn_accent_color}}

icon_color = "#fff8"


blue_font_color = "rgb(107,99,246)"
text_light_color = "#fff"
text_dark_color = "black"
text_color = "#fff"

shadow_light = "rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;"
shadow = "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"

content_width_vw = "90vw"
navbar_width = "10em"

btn_orange = "#eb7d00"
# btn_orange = "#ffa53d"


message_style = dict(display="inline-block", p="4", border_radius="xl", max_w="30em")

input_style = dict(
    bg=bg_medium_color,
    border_color=border_color,
    border_width="1px",
    p="4",
)

icon_style = dict(
    font_size="md",
    color=icon_color,
    _hover=dict(color=text_light_color),
    cursor="pointer",
    w="8",
)

sidebar_style = dict(
    border="double 1px transparent;",
    border_radius="10px;",
    background_image=f"linear-gradient({bg_dark_color}, {bg_dark_color}), radial-gradient(circle at top left, {accent_color},{accent_dark});",
    background_origin="border-box;",
    background_clip="padding-box, border-box;",
    p="2",
    _hover=dict(
        background_image=f"linear-gradient({bg_dark_color}, {bg_dark_color}), radial-gradient(circle at top left, {accent_color},{accennt_light});",
    ),
)

base_style = {
    rx.Avatar: {
        "shadow": shadow,
        "color": text_light_color,
        "bg": border_color,
    },
    rx.Button: {
        "shadow": shadow,
        "color": text_light_color,
        "_hover": {
            "bg": accent_dark,
        },
    },
    rx.Menu: {
        "bg": bg_dark_color,
        "border": f"red",
    },
    rx.MenuList: {
        "bg": bg_dark_color,
        "border": f"1.5px solid {bg_medium_color}",
    },
    rx.MenuDivider: {
        "border": f"1px solid {bg_medium_color}",
    },
    rx.MenuItem: {
        "bg": bg_dark_color,
        "color": text_light_color,
    },
    rx.DrawerContent: {
        "bg": bg_dark_color,
        "color": text_light_color,
        "opacity": "0.9",
    },
    rx.Hstack: {
        "align_items": "center",
        "justify_content": "space-between",
    },
    rx.Vstack: {
        "align_items": "stretch",
        "justify_content": "space-between",
    },
    rx.Heading: {
        "color": text_dark_color,
    },
    rx.Input: {
        "bg": bg_dark_color
    }
}


template_page_style = {"padding_top": "5em", "padding_x": ["auto", "2em"], "flex": "1"}

template_content_style = {
    # "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": btn_orange,
    "border": border,
    "border_radius": border_radius,
}

# base_style = {
#     rx.MenuButton: {
#         "width": "3em",
#         "height": "3em",
#         **overlapping_button_style,
#     },
#     rx.MenuItem: hover_accent_bg,
# }

markdown_style = {
    "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        color="#03030B",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#03030B",
        },
    ),
}

# treatment-gen
# shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
# message_style = dict(
#     padding="1em",
#     border_radius="5px",
#     margin_y="0.5em",
#     box_shadow=shadow,
# )

# Set specific styles for questions and answers.
question_style = message_style | dict(
    bg="#F5EFFE", margin_left=chat_margin
)
answer_style = message_style | dict(
    bg="#DEEAFD", margin_right=chat_margin
)

# Styles for the action bar.
# input_style = dict(
#     border_width="1px", padding="1em", box_shadow=shadow
# )
button_style = dict(bg=btn_orange, box_shadow=shadow)


# rave
index = dict(
    margin_top="100px",
    padding="2em",
    border_radius="5px",
    box_shadow="rgba(0, 0, 0, 0.15) 0px 2px 8px",
    margin_left="auto",
    margin_right="auto",
    max_width="75%", 
    background_size="cover",
    min_height="750px",
)

hero_banner_text = dict(
    text_align="center",
    margin="1em",
    color="white",

)

border = dict(
    border="2px solid black",
    color="black", 
)

select = dict(
    margin="1em",
    margin_left="auto",
    margin_right="auto",
    border="2px solid white",
)

image = dict(
    margin="1em",
    max_width="425",
    max_height="500",
)

heading = dict(
    margin="0.7em",
    font_size="1.5em"
)

card = dict(
    margin="1em",
    text_align="center",
    width="430px",
)

button = dict(
    color = btn_orange,
    margin_left="auto",
    margin_right="0",
    padding="0.5em",
    border_radius="5px",
    background="white",
)


#summerizer
style = {
    "background-color": "#454545",
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

topic_style = {
    "color": "white",
    "font_family": "Comic Sans MS",
    "font_size": "3em",
    "font_weight": "bold",
    # "box_shadow": "rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px",
    "margin-bottom": "3rem",
}

textarea_style = {
    "color": "white",
    "width": "150%",
    "height": "20em",
}


openai_input_style = {
    "color": "black",
    "margin-top": "2rem",
    "margin-bottom": "1rem",
}


submit_button_style = {
    "color" : accent_color,
    "margin-left": "30%",
}


summary_style = {
    "color": "white",
    "margin-top": "2rem",
}



#------------------------------table---------------------------------------------------------

darkTheme = {
    "accentColor": "#8c96ff",
    "accentLight": "rgba(202, 206, 255, 0.253)",
    "textDark": "#ffffff",
    "textMedium": "#b8b8b8",
    "textLight": "#a0a0a0",
    "textBubble": "#ffffff",
    "bgIconHeader": "#b8b8b8",
    "fgIconHeader": "#000000",
    "textHeader": "#a1a1a1",
    "textHeaderSelected": "#000000",
    "bgCell": "#16161b",
    "bgCellMedium": "#202027",
    "bgHeader": "#212121",
    "bgHeaderHasFocus": "#474747",
    "bgHeaderHovered": "#404040",
    "bgBubble": "#212121",
    "bgBubbleSelected": "#000000",
    "bgSearchResult": "#423c24",
    "borderColor": "rgba(225,225,225,0.2)",
    "drilldownBorder": "rgba(225,225,225,0.4)",
    "linkColor": "#4F5DFF",
    "headerFontStyle": "bold 14px",
    "baseFontStyle": "13px",
    "fontFamily": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
}


tab_style = {
    "color": "#494369",
    "font_weight": 600,
    "_selected": {
        "color": "#5646ED",
        "bg": "#F5EFFE",
        "padding_x": "0.5em",
        "padding_y": "0.25em",
        "border_radius": "8px",
    },
}