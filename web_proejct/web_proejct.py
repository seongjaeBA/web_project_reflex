"""Welcome to Reflex!."""
from web_proejct.api import product_router
from web_proejct.crawapi import crawling_router

from dotenv import load_dotenv
from web_proejct import styles

from web_proejct.pages import *

import reflex as rx


class State(rx.State):
    load_dotenv(dotenv_path='../env/.env')
    """Define empty state to allow access to rx.State.router."""
    """ vars & eventhandlers(func)
        base var input -> event trigger -> event handler -> (@rx.var)compute var
    """
    ''' global(base) vars'''

    ''' def func'''


    '''decorator & def to compute var'''
    
    """Upload DB"""

# Create the app.
app = rx.App(style=styles.base_style)
app.api.include_router(product_router)
app.api.include_router(crawling_router)
