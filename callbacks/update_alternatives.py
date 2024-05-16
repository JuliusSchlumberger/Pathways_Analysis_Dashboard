import dash
from dash import html, dcc, callback, Input, Output, State,callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import json

from dashapp import app
from utilities.generate_missing_message import generate_missing_input_message

@app.callback(
    [Output('alternatives-graph', 'children'),
Output('storage-alternative_pathways', 'data'),
     Output('risk_owner_hazard', 'value')],
    [Input('risk_owner_hazard', 'value'),
    Input('viewport-size', 'data')
     ],
State('storage-alternative_pathways', 'data'),
)
def update_options_graph(risk_owner_hazard,viewport_data, stored_data):
    # message = generate_missing_input_message(('Risk Owner - Hazard Pair', stored_data['risk_owner_hazard']))
    # print(message)
    if risk_owner_hazard is not None:   # if this is not empty
        stored_data['risk_owner_hazard'] = risk_owner_hazard
        relevant_input = risk_owner_hazard
    else:
        message = generate_missing_input_message(('Risk Owner - Hazard Pair', stored_data.get('risk_owner_hazard', None)))
        if message:
            return [html.Div(message,
                             style={'color': 'red', 'fontSize': '20px', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})], dash.no_update, dash.no_update
        # if any(input_value is None for input_value in
        #        [stored_data['risk_owner_hazard']]):
        #     return go.Figure(), dash.no_update, dash.no_update
        relevant_input = stored_data['risk_owner_hazard']

    figure_identifier = f'assets/figures/decision_tree/alternative_pathways_{relevant_input}.json'

    with open(figure_identifier, 'r') as f:
        fig = pio.from_json(f.read())

    current_width = fig.layout.width
    current_height = fig.layout.height

    size = json.loads(viewport_data)

    width, height = size['width'], size['height']
    scale_factor = min(width / 1920, height/927)  # Assuming 1920px is the standard width for full scale

    # Scale the dimensions
    scaled_width = current_width * scale_factor
    scaled_height = current_height * scale_factor

    fig.update_layout(
        width=scaled_width,
        height=scaled_height,
        autosize=False,  # Ensure that the size is set explicitly based on scaled dimensions
        title_font_size=18 * scale_factor,
        font_size=14 * scale_factor,
        # margin=dict(l=50 * scale_factor, r=50 * scale_factor, t=50 * scale_factor, b=50 * scale_factor)
    )
    return [dcc.Graph(figure=fig, responsive=True)], stored_data, relevant_input
