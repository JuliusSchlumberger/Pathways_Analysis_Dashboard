import dash
from dash import html, dcc, callback, Input, Output, State,callback_context
import plotly.io as pio
from utilities.scale_figure import scale_figure
from assets.static_inputs import INTERACTIONS

from dashapp import app
from utilities.generate_missing_message import generate_missing_input_message

@app.callback(
    [Output('alternatives-graph', 'children'),
    Output('storage-general', 'data', allow_duplicate=True),
     Output('risk_owner_hazard', 'value'),
     ],
    [Input('risk_owner_hazard', 'value'),
     ],
State('storage-general', 'data'),
prevent_initial_call=True
)
def update_options_graph(risk_owner_hazard, stored_data):
    print('alternatives', stored_data)
    if risk_owner_hazard is not None:   # if this is not empty
        stored_data['risk_owner_hazard'] = risk_owner_hazard
        filtered_options = [{'label': key, 'value': value} for option in INTERACTIONS[risk_owner_hazard] for key, value
                            in
                            option.items()]
        stored_data['interactions'] = filtered_options
        relevant_input = risk_owner_hazard
    else:
        message = generate_missing_input_message(('Risk Owner - Hazard Pair', stored_data.get('risk_owner_hazard', None)))
        if message:
            return [html.Div('Specify the focus of the analysis (see left), to see a visualization',
                             style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})], dash.no_update, dash.no_update
        relevant_input = stored_data['risk_owner_hazard']

    figure_identifier = f'assets/figures/decision_tree/alternative_pathways_{relevant_input}.json'

    with open(figure_identifier, 'r') as f:
        fig = pio.from_json(f.read())

    fig, _, _ = scale_figure(fig, stored_data)

    return [dcc.Graph(figure=fig, responsive=False)], stored_data, relevant_input


