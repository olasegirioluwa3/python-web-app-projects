import dash_html_components as html

layout = html.Div([
    html.H1('Home'),
    # Add page content here
])
# Define the layout for the product show page
layout = html.Div([
    html.H1('Product Details'),  # Title
    html.Div([
        # Product Image
        html.Img(src='product_image_url.jpg', alt='Product Image', width='300px'),

        # Product Description
        html.Div([
            html.H2('Product Name'),
            html.P('Product Description: This is a fantastic product with great features.'),
            html.P('Price: $99.99'),
            html.Button('Add to Cart', id='add-to-cart-button'),
        ], style={'margin-left': '20px'}),
    ], style={'display': 'flex'}),

    # Additional product information, reviews, etc.
    html.Div([
        html.H3('Product Information'),
        # Add more product information here

        html.H3('Product Reviews'),
        # Add product reviews or ratings here
    ]),
])
