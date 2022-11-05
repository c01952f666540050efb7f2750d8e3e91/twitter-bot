# Dash imports
from dash import Dash, dcc, html, Input, Output, State, dcc, ctx
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

# General Imports
import os
from ctypes.wintypes import PINT
import requests as req
from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session
import json
import flask

# Internal imports
from components import *

token_req = False
# How we want this to work:
# We have a link in the navbar top right - asking if you want to login
# if you select the link, you're taken to the correct page so that
# you can input your pin
# once you've done that, the pin input dissappears and you will be navigated to
# the twitter dashboard accordingly

# Added dark theme
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.DARKLY],
    use_pages=True
)


# We will want to make multiple callbacks
# The first will be for authentication and to begin running the bot
# We will want to know how close we are to the rate limit as well as
# Who we're responding to
# It will be nice to know what kind of scams are out there as well

# Callback to begin bot loop - TODO
# @app.callback(
#     Output(component_id="main-window", component_property="children"),
#     [
#         Input("pin-request", "n_clicks")
#     ],
#     prevent_initial_call = False
# )
# def runBot(clickNumber):
#     return None

# Main app layout
app.layout = html.Div(children=[
    navbar,
    dash.page_container
])

for page in dash.page_registry.values():
    print(page)


# To Run, use below:
app.run_server(debug=True)
