import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
# from dash_bootstrap_components import dbc
import dash_bootstrap_components as dbc
import pages.home  # Import your page layouts
import pages.page1  # Import your page layouts
import pages.page2
import pages.page3
import pages.page4
import pages.page5
import pages.page6
import page404
import components.navbar

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/assets/styles/styles.css'])


# Create the navbar using the create_navbar function
navbar_layout = components.navbar.create_navbar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(navbar_layout),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return pages.home.layout
    elif pathname == '/page1':
        return pages.page1.layout
    elif pathname == '/page2':
        return pages.page2.layout
    elif pathname == '/page3':
        return pages.page3.layout
    elif pathname == '/page4':
        return pages.page4.layout
    elif pathname == '/page5':
        return pages.page5.layout
    elif pathname == '/page6':
        return pages.page6.layout
    else:
        return page404.layout

if __name__ == '__main__':
    app.run_server(debug=True)
