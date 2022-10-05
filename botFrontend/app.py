from dash import Dash, dcc, html, Input, Output, dcc


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Ledger Protect Twitter Bot Frontend (v0.01)"),
    html.Div([
        "Input: ",
        dcc.Input(id="pin-code", value="PIN Code", type="text")
    ]),
    html.Br(),
    html.Div(id="app")
])

@app.callback(
    Output(component_id="app", component_property="children"),
    Input(component_id="pin-code", component_property="value")
)
def providePinCode(inputValue):
    return f'Pin Code {inputValue}'

# To Run, use below:
app.run_server(debug=True)