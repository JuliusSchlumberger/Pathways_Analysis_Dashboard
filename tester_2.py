from dash import Dash, html, dcc, callback, Input, Output, State, ctx

# Initialize the Dash app
app = Dash(__name__)

# Define the layout for each page
page_layouts = {
    '/page-1': html.Div([
        html.H3('This is Page 1'),
        html.P('Content for Page 1')
    ]),
    '/page-2': html.Div([
        html.H3('This is Page 2'),
        html.P('Content for Page 2')
    ]),
    '/page-3': html.Div([
        html.H3('This is Page 3'),
        html.P('Content for Page 3')
    ])
}

# Layout of the app
app.layout = html.Div([
    # dcc.Location to handle URLs
    dcc.Location(id='url', refresh=False),

    # Navigation bar
    html.Div([
        dcc.Link('Page 1', href='/page-1', className='nav-link'),
        dcc.Link('Page 2', href='/page-2', className='nav-link'),
        dcc.Link('Page 3', href='/page-3', className='nav-link'),
        html.Button('Previous', id='prev-button', n_clicks=0, className='nav-button'),
        html.Button('Next', id='next-button', n_clicks=0, className='nav-button'),
    ], className='navbar'),

    # Content area where pages will be displayed
    html.Div(id='page-content'),

    # Store current page index in hidden div
    dcc.Store(id='current-page-index', data=0)
])


# Define the callback to update the page content based on the URL or button clicks
@app.callback(
    Output('page-content', 'children'),
    Output('current-page-index', 'data'),
    Input('url', 'pathname'),
    Input('prev-button', 'n_clicks'),
    Input('next-button', 'n_clicks'),
    State('current-page-index', 'data')
)
def display_page(pathname, prev_clicks, next_clicks, current_index):
    # Define page keys
    page_keys = list(page_layouts.keys())
    max_index = len(page_keys) - 1

    # If pathname in URL is in page_layouts, update the current_index accordingly
    if pathname in page_layouts:
        current_index = page_keys.index(pathname)
    else:
        pathname = page_keys[current_index]

    # Determine which button was clicked
    triggered = ctx.triggered_id

    if triggered == 'prev-button' and current_index > 0:
        current_index -= 1
    elif triggered == 'next-button' and current_index < max_index:
        current_index += 1

    # Get the layout for the current page based on current index
    page_key = page_keys[current_index]
    return page_layouts[page_key], current_index


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
