import dash
from dash import Dash, dcc, html, Input, Output, State, dcc, ctx, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/auth",
    title="Authorise",
    name="Authorisation Page"
)


layout = html.Div(
    id="auth-content"
)