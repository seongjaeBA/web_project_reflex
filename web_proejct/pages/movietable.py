import web_proejct.styles as styles
from web_proejct.templates import template
from web_proejct.state import DataTableLiveState, DataTableState, KMDBTableLiveState

import reflex as rx

def LiveTable() -> rx.Component:
    return rx.vstack(
            rx.stack(
                rx.cond(
                    ~DataTableLiveState.running,
                    rx.button(
                        "Start",
                        on_click=DataTableLiveState.toggle_pause,
                        color_scheme="green",
                    ),
                    rx.button(
                        "Pause",
                        on_click=DataTableLiveState.toggle_pause,
                        color_scheme="red",
                    ),
                ),
            ),
            rx.data_editor(
                columns=DataTableLiveState.columns,
                data=DataTableLiveState.table_data,
                draw_focus_ring=True,
                row_height=50,
                smooth_scroll_x=True,
                smooth_scroll_y=True,
                column_select="single",
                # style
                theme=styles.darkTheme,
            ),
            overflow_x="auto",
            width="100%",
    )
    
def CrawTable() -> rx.Component:
    return 
    


@template(route = "/MovieTable", title = "무비 테이블")
def MovieRank() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Movie Rank Table", font_size="2em", color = "white"),
            rx.vstack(
                rx.tabs(
                    rx.tab_list(
                        rx.tab("Static Data", style=styles.tab_style),
                        rx.tab("Live Data", style=styles.tab_style),
                        rx.tab("Scenario Search", style=styles.tab_style),
                    ),
                    rx.tab_panels(
                        rx.tab_panel(
                            rx.vstack(
                                rx.button("크롤링 시작", on_click=DataTableState.set_dailyrank),
                                rx.heading(DataTableState.clicked_cell, size="sm", color="blue"),
                                rx.heading(DataTableState.edited_cell, size="sm", color="green"),
                                rx.heading(DataTableState.right_clicked_group_header, size="sm", color="orange",),
                                rx.heading(DataTableState.item_hovered, size="sm", color="purple",),
                                rx.heading(DataTableState.deleted, size="sm", color="red"),
                                rx.data_editor(
                                    columns=DataTableState.cols,
                                    data=DataTableState.table_data,
                                    # rows=10,
                                    on_paste=True,
                                    draw_focus_ring=False,
                                    # fixed_shadow_x=True,
                                    freeze_columns=2,
                                    group_header_height=100,
                                    header_height=80,
                                    # max_column_auto_width=200,
                                    # this works just need to describe it
                                    # max_column_width=200,
                                    min_column_width=100,
                                    row_height=50,
                                    row_markers="clickable-number",
                                    # also mention smooth_scroll_y
                                    smooth_scroll_x=True,
                                    vertical_border=False,
                                    column_select="multi",
                                    # prevent_diagonal_scrolling=False,
                                    overscroll_x=0,
                                    on_cell_clicked=DataTableState.get_clicked_data,
                                    on_cell_edited=DataTableState.get_edited_data,
                                    on_group_header_context_menu=DataTableState.get_group_header_right_click,
                                    on_item_hovered=DataTableState.get_item_hovered,
                                    on_delete=DataTableState.get_deleted_item,
                                    # on_row_appended=DataTableState.append_row,
                                    on_column_resize=DataTableState.column_resize,
                                    theme=styles.darkTheme,
                                    width="80vw",
                                    height="80vh",
                                ),
                            ),
                        ),
                        rx.tab_panel(
                            LiveTable()
                        ),
                        rx.tab_panel(
                            # APITable()
                            rx.vstack(
                                rx.stack(
                                    rx.input(
                                        placeholder="검색어",
                                        on_change=KMDBTableLiveState.set_keyword
                                    ),
                                    rx.button(
                                        "Start",
                                        on_click=KMDBTableLiveState.get_movieinfo,
                                        color_scheme="green",
                                    ),
                                ),
                            ),
                            rx.data_editor(
                                columns=KMDBTableLiveState.columns,
                                data=KMDBTableLiveState.table_data,
                                draw_focus_ring=True,
                                row_height=50,
                                smooth_scroll_x=True,
                                smooth_scroll_y=True,
                                column_select="single",
                                # style
                                theme=styles.darkTheme,
                            ),
                            overflow_x="auto",
                            width="100%",
                        ),
                        
                    ),
                    spacing="1.5em",
                    font_size="2em",
                    padding_top="10vh",
                    width="90vw",
                ),
            ),
        ),
    )