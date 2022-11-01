# Dash Imports
import dash
from dash import Dash, dcc, html, Input, Output, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

dash.register_page(__name__, path="/auth")

authContent = html.Div(
    children=[
        'this is content'
    ]
)