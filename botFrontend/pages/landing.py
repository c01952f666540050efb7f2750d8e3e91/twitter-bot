from dash import dcc, html, Input, Output, dcc, ctx, register_page, callback
import dash_bootstrap_components as dbc

import os
from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session
import json
import flask

# Load .env
load_dotenv(dotenv_path="../")
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
base_authorization_url = "https://api.twitter.com/oauth/authorize"
access_token_url = "https://api.twitter.com/oauth/access_token"

resource_owner_key = None
resource_owner_secret = None

# Register Page
register_page(
    __name__,
    path="/"
)

# pin_request = 

layout = html.Div(children=[
    html.H2(
        "You have not authorised this application",
        style={'textAlign': 'center'}
    ),
    html.P(
        [
            "Please press the below button to get the correct URL. You'll be then",
            html.Br(),
            "provided with a link where which will create a new tab. You will need to",
            html.Br(),
            "authorise this application, as well as provide the pin above."
        ],
        style={'textAlign': 'center'}
        ),
    html.Center(
        dbc.Table(
            [
                html.Tr([
                    html.Td(
                        dbc.Button(
                            "Get URL",
                            id="pin-request",
                            color="primary",
                            className="ms-1",
                            n_clicks=0
                        ),
                        style={
                            'textAlign': 'right'
                        }
                    ),
                    html.Td(
                        # Input PIN
                        dbc.Input(
                            id="pin-code",
                            type="password", 
                            # className="primary",
                            placeholder="Enter PIN here"
                        ),
                        style={
                            'width': '10%'
                        }
                    ),
                    html.Td(
                        # Submit Button
                        dbc.Button(
                            "Submit", 
                            id="pin-submit-button",
                            color="primary", 
                            className="ms-1", 
                            n_clicks=0
                        )
                    )
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(
                        id="auth-content",
                        rowSpan="3",
                        style={
                            "textAlign": "center"
                        }
                    ),
                    html.Td()
                ])
            ],
            bordered=False
        )
    )  
])

# Callback for getting Auth 
@callback(
    Output(component_id="auth-content", component_property="children"),
    [
        Input("pin-request", "n_clicks")
    ],
    # Do not immediately initialise
    prevent_initial_call = False
)
def contentWindowManager(clickNumber):
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
            ),

        # set key and secret
        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        # Update bool
        token_req = True

        # Get Auth URL - redirect here
        authorization_url = oauth.authorization_url(base_authorization_url)

        # Temp print
        print("clicked!")

        return html.Div(
            children=[
                dcc.Link(
                    "Authorise",
                    href=authorization_url,
                    target="_blank"
                )
            ]
        )

    # Return Nothing when nothing is pressed
    return None

@callback(
    Output(component_id="placeholder-000", component_property="children"),
    [
        Input("pin-submit-button", "n_clicks"),
        Input("pin-code", "value")
    ],
    # Do not immediately initialise
    prevent_initial_call = False
)
def pinSubmit(nClicks, pinValue):
    # Finish completing the authorisation
    oauth = OAuth1Session(
        agent_key,
        client_secret=agent_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=pinValue,
    )

    oauth_tokens = oauth.fetch_access_token(access_token_url)

    oauth = OAuth1Session(
        agent_key,
        client_secret=agent_secret,
        resource_owner_key=oauth_tokens["oauth_token"],
        resource_owner_secret=oauth_tokens["oauth_token_secret"],
    )

    return