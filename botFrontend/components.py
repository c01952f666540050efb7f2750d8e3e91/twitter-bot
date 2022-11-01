# Dash Imports
from dash import Dash, dcc, html, Input, Output, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

# Image Imports
import base64

# Ledger Logo
logo_fp = r"assets/ledger_logo.jpg"
encoded_image = base64.b64encode(open(logo_fp, 'rb').read())

# All the main components to be imported into app.py
# Enter PIN object
pin_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(
            id="pin-code",
            type="password", 
            placeholder="Enter PIN"
            )),
        dbc.Col(
            dbc.Button(
                "Submit", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

pin_request = dbc.Button(
    "Get PIN",
    id="pin-request",
    color="primary",
    className="ms-2",
    target="contentContainer",
    n_clicks=0
)

# Nav Bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=logo_fp, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Ledger Protect Twitter Bot Frontend (v0.01)", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="http://localhost:8050", # Go back to home screen
                style={"textDecoration": "none"},
            ),
            # Update the below so it only shows when required - we will need to get the state of the oauth login somehow
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            pin_request,  # Use this as link to get PIN on mainscreen
            pin_bar
        ]
    ),
    color="dark",
    dark=True
)

