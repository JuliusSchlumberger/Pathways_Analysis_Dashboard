import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, ClientsideFunction, clientside_callback
from pages import *
from components import sidebar, content, header, TermsConditions
# from callbacks import toggle_tabs
import dash
from callbacks import (navigation_pages, update_alternatives, add_legend, \
    toggle_robustness_figure, update_robustness, \
    update_multi_sector_interactions, update_interaction_plot, submit_responses_db, update_pathways,\
     toggle_termsconditions, update_surveys, toggle_word_explanations, update_figure_description, update_drop_down, to_store,

                       validate_answers)

from dashapp import app


server = app.server
app.layout = dbc.Container([
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='storage-general', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='viewport-size'),  # To store and use viewport data in other callbacks
        header.header,
        html.Div(id='page-content'),
        html.Div(id='document-title', style={'display': 'none'}),  # Hidden div for setting the document title
        # dash.page_container,  # This will display the content of the current page
        # TermsConditions.TermConditions,


],
    fluid=True,  # Change to 100vh to fill the screen height
)

# Clientside function to capture viewport size
clientside_callback(
    """
    function(trigger) {
        return {
            width: window.innerWidth,
            height: window.innerHeight
        };
        
    }
    """,
    Output('viewport-size', 'data'),
    Input('url', 'href')
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