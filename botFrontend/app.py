from ctypes.wintypes import PINT
from dash import Dash, dcc, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import base64

# How we want this to work:
# We have a link in the navbar top right - asking if you want to login
# if you select the link, you're taken to the correct page so that
# you can input your pin
# once you've done that, the pin input dissappears and you will be navigated to
# the twitter dashboard accordingly


# Added dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Ledger Logo
logo_fp = r"assets/ledger_logo.jpg"
encoded_image = base64.b64encode(open(logo_fp, 'rb').read())


# Search Bar
pin_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="password", placeholder="Enter PIN")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
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
                href="http://localhost:8050",
                style={"textDecoration": "none"},
            ),
            # Update the below so it only shows when required - we will need to get the state of the oauth login somehow
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.NavItem(dbc.NavLink("Get PIN", href="#")),
            dbc.Collapse(
                pin_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True
)

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# button callback
@app.callback(
    Output('app2', 'children'),
    Input('pin-code', 'value')
)
def update_output(value):
    return [f'The input value was {value}']


# Current input DIV
app.layout = html.Div([
    navbar,
    html.Div([
        "Input: ",
        dcc.Input(
            id="pin-code", 
            placeholder="PIN Code", 
            type="password"
            )
    ]),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Div(id="app"),
    html.Div(id="app2")
])

# Current SHOW PIN div - testing
@app.callback(
    Output(component_id="app", component_property="children"),
    Input(component_id="pin-code", component_property="value")
)
def providePinCode(inputValue):
    # function that will return the PIN Code
    # Think about processing this within function?
    return f'Pin Code {inputValue}'

# @app.callback(
#     Output(component_id="oauth-link", component_property="children"),
#     Input(component_id="")
# )
# def testCallback():
#     return None

# We will want to make multiple callbacks
# The first will be for authentication and to begin running the bot
# We will want to know how close we are to the rate limit as well as
# Who we're responding to
# It will be nice to know what kind of scams are out there as well

# To Run, use below:
app.run_server(debug=True)
