import dash_html_components as html
import dash_bootstrap_components as dbc

# Create a function that returns the navbar layout
def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            dbc.NavItem(dbc.NavLink("Page 3", href="/page3")),
            # Add more navigation links as needed
        ],
        brand="COD Show Room",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar
