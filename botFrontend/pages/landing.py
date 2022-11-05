from dash import dcc, html, Input, Output, dcc, ctx, register_page, callback
import dash
import dash_bootstrap_components as dbc

# internal import
from app import twitterAuth

# Register Page
register_page(
    __name__,
    path="/"
)

# Layout
layout = html.Div(children=[
    # title
    html.H2(
        "You have not authorised this application",
        style={'textAlign': 'center'}
    ),
    # Main text
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
                        style={
                            "textAlign": "center"
                        }
                    ),
                    html.Td()
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(
                        id="landing-content",
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
       
        
        # Get Auth URL - redirect here
        authorization_url = twitterAuth.getAuthURL()

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
    return html.Div(
        children=[
            html.Br()
        ]
    )

@callback(
    Output(component_id="landing-content", component_property="children"),
    [
        Input("pin-submit-button", "n_clicks"),
        Input(component_id="pin-code", component_property="value")
    ],
    # Do not immediately initialise
    prevent_initial_call = True
)
def pinSubmit(nClicks, pinValue):

    # If button is clicked
    if "pin-submit-button" == ctx.triggered_id:
        twitterAuth.submitPin(pinValue)

        # TODO - Find out what we want to return - otherwise we will create class
        return html.Div(
            children=[
                dcc.Link(
                    "Go to dashboard",
                    id="landing-content",
                    href=dash.page_registry['pages.dashboard']['path']
                )
            ]
        )
    
    return html.Div(
        children=[
            html.Br()
        ]
    )