from dash import Dash, dcc, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import base64

# Added dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Ledger Logo
logo_fp = r"assets/ledger_logo.jpg"
encoded_image = base64.b64encode(open(logo_fp, 'rb').read())


# Search Bar
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
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
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
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
    html.Br(),
    html.Div(id="app")
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
