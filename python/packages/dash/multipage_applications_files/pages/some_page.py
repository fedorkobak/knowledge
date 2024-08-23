import dash
from dash import html, callback, Input, Output

import pickle

dash.register_page(__name__)
layout = html.Div([
    html.H1('Page with button'),
    html.Button(
        "Save page_registry",
        id="save-button",
    ),
    html.Div(id='dummy')
])

@callback(
    Output("dummy", "children"),
    Input("save-button", "n_clicks")
)
def save_callback(n_clicks):
    with open("page_registry", "wb") as f:
        pickle.dump(dash.page_registry, f)
