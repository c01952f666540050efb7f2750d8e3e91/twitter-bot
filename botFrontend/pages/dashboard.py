# dash imports
import dash
from dash import dcc, html, Input, Output, dcc, ctx, register_page, callback
import dash_bootstrap_components as dbc

# dotenv imports
from dotenv import load_dotenv
import os

# Load .env
load_dotenv(dotenv_path="../.env")

# internal import
from app import twitterAuth

bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

# Register Page
dash.register_page(__name__, path="/dashboard")

# Table definition
tableHeader = html.Thead(html.Tr(
    html.Th(
        html.H3(
            "Dashboard",
            style={'textAlign': 'center'}
        )
    )
))
row1 = html.Tr(
    children=[
        html.Td(

        ),
        html.Td(
            
        )
    ]
)

twitterTable = dbc.Table(
    tableHeader,

)

# Layout
layout = html.Div(
    [
        twitterTable
    ]
)

# Create button to begin bot
# Create posting function and time loop with callback
# Create live data table and saving option for what we're interacting with
# Potentially option customise
# - customise rules
# - customise response
# - manually answer if want to