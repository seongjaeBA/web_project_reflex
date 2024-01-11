"""Welcome to Reflex!."""

from web_proejct import styles

# Import all the pages.
from web_proejct.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    """ vars & eventhandlers(func)
        base var input -> event trigger -> event handler -> (@rx.var)compute var
    """
    ''' global(base) vars'''

    ''' def func'''


    '''decorator & def to compute var'''

# Create the app.
app = rx.App(style=styles.base_style)
