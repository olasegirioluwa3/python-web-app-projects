from dash import html

layout = html.Div(
    className='error-container',
    children=[
        html.H1('404 - Page Not Found', style={'color': 'red'}),
        html.P("Sorry, the page you are looking for does not exist."),
        html.Img(src='/assets/images/404_animation.gif', alt='404 Not Found', style={'width': '300px', 'height': '300px'}),
    ]
)