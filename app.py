import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, ALL, State
from pages import *
from components import header, TermsConditions
from components.progress_modal import PROGRESS_MODAL
# from callbacks import toggle_tabs
import dash
from callbacks import (navigation_pages, toggle_termsconditions,
                       to_store,
                       update_alternatives, \
                       update_robustness, \
                       update_multi_sector_interactions, update_pathways, \
                       toggle_termsconditions, update_surveys, toggle_word_explanations, update_figure_description

                       )

from dashapp import app

server = app.server
app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        html.Link(rel='shortcut icon', href='/assets/favicon.ico'),
        dcc.Store(id='storage-general', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='viewport-size'),  # To store and use viewport data in other callbacks
        header.header,
        html.Div(id='page-content'),
        html.Div(id='document-title', style={'display': 'none'}),  # Hidden div for setting the document title
        dcc.Store(id='to_store-complete', data=False),
        # html.Div(id='submit-survey'),
        TermsConditions.TermConditions,
        PROGRESS_MODAL
    ],
    fluid=True,  # Change to 100vh to fill the screen height
)

app.layout.children.append(html.Div(id='dummy-output', style={'display': 'none'}))

# Clientside function to capture viewport size
app.clientside_callback(
    """
    function(trigger) {
        return {
            width: window.innerWidth,
            height: window.innerHeight
        };

    }
    """,
    Output('viewport-size', 'data'),
    [
    Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks'),
    Input('prev-btn', 'n_clicks'),
    Input('next-btn', 'n_clicks'),
    Input('url', 'pathname'),
    ],
)



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



# clientside_callback(
#     """
#     function(trigger) {
#         return JSON.stringify({
#             width: window.innerWidth,
#             height: window.innerHeight
#         });
#
#     }
#     """,
#     Output('viewport-size', 'data'),
#     Input('viewport-size', 'n_intervals')
# )


if __name__ == '__main__':
    app.run_server(debug=True)