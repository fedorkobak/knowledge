from dash import Dash, html

app = Dash(__name__, requests_pathname_prefix='/dash/')
app.layout = html.Div("Hello world")

server = app.server

if __name__ == "__main__":
	app.run_server(debug=True, port=8051)
