# Dash imports
from dash import Dash, dcc, html, Input, Output, State, dcc, ctx
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

# Load .env
load_dotenv(dotenv_path="../")
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
base_authorization_url = "https://api.twitter.com/oauth/authorize"

token_req = False
# How we want this to work:
# We have a link in the navbar top right - asking if you want to login
# if you select the link, you're taken to the correct page so that
# you can input your pin
# once you've done that, the pin input dissappears and you will be navigated to
# the twitter dashboard accordingly

# Added dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

@app.callback(
    Output(component_id="main-window", component_property="children"),
    [
        Input("pin-request", "n_clicks")
    ],
    prevent_initial_call = False
)
def contentWindowManager(clickNumber):
    msg = "button not pressed"
    authorization_url=""

    

    # When Request PIN Button is pressed
    if "pin-request" == ctx.triggered_id:
        # Get Request token
        oauth = OAuth1Session(agent_key, client_secret=agent_secret)

        # Attempt to fetch
        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        # set key and secret
        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        # Update bool
        token_req = True

        # Get Auth URL - redirect here
        authorization_url = oauth.authorization_url(base_authorization_url)

        # Temp print
        print("clicked!")

        return dbc.Container(
            html.Div(
                id="contentContainer"
            )
        )

    return html.Div(
        "Nothing"
    )
    # return html.Div(
    #         "html.A("Open to Authorise", href=authorization_url, target="_blank")"
    #     )


# We will want to make multiple callbacks
# The first will be for authentication and to begin running the bot
# We will want to know how close we are to the rate limit as well as
# Who we're responding to
# It will be nice to know what kind of scams are out there as well

# Main app layout
app.layout = html.Div([
    navbar,
    html.Br(),
    html.Div(id="main-window")
])

# To Run, use below:
app.run_server(debug=True)
