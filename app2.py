# ... [rest of the imports and app initialization]
import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash import Dash
from dash.dependencies import Input, Output
from flask import Flask, send_from_directory

server = Flask(__name__, static_folder='static')
app = Dash(__name__, server=server)

@server.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the sidebar layout
SIDEBAR_STYLE = {
    "padding": "20px 10px",
    "background-color": "#f8f9fa",
    "border": "1px solid #dee2e6"
}

sidebar = html.Div(
    [
        html.Hr(),
        html.H5("Input Numbers"),
        dbc.Input(id="input-1", type="number", placeholder="Enter first number", className="mb-2"),
        dbc.Input(id="input-2", type="number", placeholder="Enter second number", className="mb-2"),
    ],
    style=SIDEBAR_STYLE
)

# Main content area layout remains unchanged
content = html.Div(
    [
        html.Img(src="/static/logo.png", height="100px"),
        html.Img(src="/static/cover.gif", height="300px"),
        html.H1(id="output-display", className="mt-4")
    ],
    className="ml-4"
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=4),
                dbc.Col(content, width=8)
            ]
        ),
    ],
    className="mt-4", fluid=True
)

@app.callback(
    Output("output-display", "children"),
    Input("input-1", "value"),
    Input("input-2", "value")
)
def update_output(val1, val2):
    if val1 and val2:
        result = val1 + val2
        return f"Result: {result}"
    return "Enter numbers to get a result."

# ... [rest of the app configuration and main function]

if __name__ == "__main__":
    app.run_server(debug=True)