
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html, ClientsideFunction, clientside_callback
from components import sidebar, content, header, TermsConditions
# from callbacks import toggle_tabs
import dash
from callbacks import toggle_glossary, toggle_tabs, update_alternatives, add_legend, \
    toggle_performance_explanation, toggle_performance_figure, update_performance, \
    update_multi_sector_interactions, update_interaction_plot, submit_responses, update_survey_tab_title, generate_session_id, toggle_termsconditions, update_surveys, viewport_size

from dashapp import app

server = app.server
app.layout = dbc.Container([
        # dcc.Interval(id='interval-component', interval=1000, n_intervals=0),  # checks every second
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='storage-alternative_pathways', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-pathways_performance', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-interactions', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-general', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='viewport-size'),  # To store and use viewport data in other callbacks
        header.header,
        TermsConditions.TermConditions,
        dbc.Row([sidebar.sidebar,
                 content.content], className="mb-0", id="content", style={"display": "none", 'height': '90vh'}),
    ],
    fluid=True, style={'height': '100vh'},  # Change to 100vh to fill the screen height
)

# app.layout.children.append(html.Div(id='dummy-div', style={'display': 'none'}))

# Clientside function to capture viewport size
clientside_callback(
    """
    function(trigger) {
        return JSON.stringify({
            width: window.innerWidth,
            height: window.innerHeight
        });
    }
    """,
    Output('viewport-size', 'data'),
    Input('viewport-size', 'n_intervals')
)


# app.clientside_callback(
#     """
#     function(data) {
#         return data;
#     }
#     """,
#     Output('output-component', 'children'),  # Change this to your target output
#     Input('viewport-size', 'data')
# )
#
#
#
# @app.callback(
#     Output('dummy-div', 'children'),  # Dummy output, not used
#     Input('viewport-size', 'data')
# )
# def print_viewport_sizes(data):
#     if data is not None:
#         vh_in_pixels = data['vh']
#         vw_in_pixels = data['vw']
#         print(f"Viewport Height: {vh_in_pixels} pixels, Viewport Width: {vw_in_pixels} pixels")
#     else:
#         print("called but empty")
#     return None  # Dummy return, as the output is not visible or used
#

# # Clientside function to capture viewport size
# clientside_callback(
#     """
#     function(trigger) {
#         return JSON.stringify({
#             width: window.innerWidth,
#             height: window.innerHeight
#         });
#     }
#     """,
#     Output('viewport-size', 'data'),
#     Input('viewport-size', 'n_intervals')
# )
#
# @app.callback(
#     Output('dynamic-figure', 'figure'),
#     Input('viewport-size', 'data')
# )
# def update_figure(viewport_data):
#     if viewport_data:
#         size = json.loads(viewport_data)
#         width, height = size['width'], size['height']
#         # Adjust figure dimensions based on the viewport size
#         fig = go.Figure(data=[go.Bar(x=["A", "B", "C"], y=[1, 3, 2])])
#         fig.update_layout(width=width*0.8, height=height*0.8)  # Example scaling
#         return fig
#     return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)