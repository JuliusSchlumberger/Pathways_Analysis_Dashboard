import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, ALL
from components import header, TermsConditions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL
from callbacks import (navigation_pages, toggle_termsconditions,
                       to_store, update_general_store,
                       update_alternatives, \
                       update_robustness, \
                       update_pathways, update_surveys, toggle_word_explanations, update_figure_description,
                       toggle_system_analysis_legend, update_figure_system_analysis, update_system_analysis_layout
                       )

from dashapp import app


server = app.server


app.layout = dbc.Container(
    [
        dcc.Store(id='viewport-size', storage_type='session', data={}),  # To store and use viewport data in other callbacks
        dcc.Store(id='store-page-A-selection', data={}),
        dcc.Store(id='store-page-A-form', data={}),
        dcc.Store(id='store-page-B-selection', data={}),
        dcc.Store(id='store-page-B-form', data={}),
        dcc.Store(id='store-page-C-selection', data={}),
        dcc.Store(id='store-page-C-form', data={}),
        dcc.Store(id='store-page-D-selection', data={}),
        dcc.Store(id='store-page-D-form', data={}),
        dcc.Store(id='store-page-E-selection', data={}),
        dcc.Store(id='store-page-E-form', data={}),
        dcc.Location(id='url', refresh=False),
        html.Link(rel='shortcut icon', href='/assets/favicon.ico'),
        dcc.Store(id='storage-general', storage_type='session', data={'current_url': '/0-introduction'}),  # Using session storage
        dcc.Store(id='storage-navigation', storage_type='session', data={}),  # Using session storage

        header.header,
        html.Div(id='page-content'),
        html.Div(id='document-title', style={'display': 'none'}),  # Hidden div for setting the document title
        dcc.Store(id='to_store-complete', data=False),

        # html.Div(id='submit-survey'),
        TermsConditions.TermConditions,
        PROGRESS_MODAL,
        FINAL_MODAL
    ],
    fluid=True,  # Change to 100vh to fill the screen height
)

app.layout.children.append(html.Div(id='dummy-output', style={'display': 'none'}))

# Clientside function to capture viewport size
app.clientside_callback(
    """
    function(trigger) {
        console.log('Callback triggered!');  // Log a message to the console
        console.log('Trigger value:', trigger);  // Log the input trigger value
        console.log(window.innerWidth, window.innerHeight);

        return {
            width: window.innerWidth,
            height: window.innerHeight
        };
    }
    """,
    Output('viewport-size', 'data'),
    [
        Input('termsconditions', 'is_open'),
    Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks'),
    Input('prev-btn', 'n_clicks'),
    Input('next-btn', 'n_clicks'),
    Input('url', 'pathname')
    ],
)

# @app.callback(
#     Output('storage-general', 'data'),
#     Input('viewport-size', 'data'),
#     State('storage-general', 'data'),
# prevent_inital_call=True
# )
# def store_viewport(viewport, stored_data):
#     # print(viewport)
#     stored_data['viewport_size'] = viewport
#     return stored_data


# Clientside callback to scroll to the top
app.clientside_callback(
    """
    function(url) {
        var element = document.getElementById('scrollable-column');
        if (element) {
            element.scrollTop = 0;  // Scroll to the top
        }
    }
    """,
    Output('dummy-output', 'children'),
    [Input('prev-btn', 'n_clicks'),
     Input('next-btn', 'n_clicks'),
     Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks'),],
)



if __name__ == '__main__':
    app.run_server(debug=True)