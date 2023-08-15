from dash import dcc, html, Input, Output, callback, Dash
from jupyter_dash import JupyterDash

app = Dash(__name__)

check_values = ["value1", "value2", "value3"]

app.layout = html.Div([
    html.Div(id='dummy'),
    dcc.Checklist(
        check_values,
        id = "check-lst"
    )
])

clicks_counter = 0

@callback(
    Output("dummy", "children"),
    Input("check-lst", "value")
)
def test_callback(checklist_value):
    global clicks_counter
    clicks_counter += 1

    print("==========================")
    print(f"    CLICK {clicks_counter}     ")
    print("==========================")
    
    print("-------value-------")
    print(checklist_value)
    return None

if __name__ == '__main__':
    app.run_server(debug=False)