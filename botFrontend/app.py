# Dash imports
from dash import Dash, html
import dash
import dash_bootstrap_components as dbc

# General Imports

# Internal imports
from components import navbar
from twitterLibs import auth

# Create authorisation object
twitterAuth = auth.authorisation()

# Added dark theme
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.DARKLY],
    use_pages=True
)

# Main app layout
app.layout = html.Div(children=[
    navbar,
    dash.page_container
])


# To Run, use below:
app.run_server(debug=True)