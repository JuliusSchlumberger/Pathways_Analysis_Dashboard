import dash
from dash import html, dcc, callback, Input, Output, State,callback_context
import plotly.io as pio
from utilities.scale_figure import scale_figure
from assets.static_inputs import INTERACTIONS
from scripts.DecisionTree.DecisionTree import decision_tree
from scripts.main_central_path_directions import FILTER_CONDITIONS, DIRECTORY_MEASURE_LOGOS, INPUT_ALTERNATIVES
from dashapp import app
from utilities.generate_missing_message import generate_missing_input_message

@app.callback(
    [Output('alternatives-graph', 'children'),
    Output('store-page-B-selection', 'data'),
     Output('risk_owner_hazard', 'value'),
     ],
    [Input('risk_owner_hazard', 'value'),
     ],
State('storage-general', 'data'),
    State('viewport-size', 'data'),
)
def update_options_graph(risk_owner_hazard, stored_data, viewport):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('alternatives', triggered_id, stored_data)
    if risk_owner_hazard is not None:   # if this is not empty
        storage['risk_owner_hazard'] = risk_owner_hazard
        filtered_options = [{'label': key, 'value': value} for option in INTERACTIONS[risk_owner_hazard] for key, value
                            in
                            option.items()]
        # stored_data['interactions'] = filtered_options
        relevant_input = risk_owner_hazard
    else:
        message = generate_missing_input_message(('Risk Owner - Hazard Pair', stored_data.get('risk_owner_hazard', None)))
        if message:
            return [html.Div('Specify the focus of the analysis (see left), to see a visualization',
                             style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})], dash.no_update, dash.no_update
        relevant_input = stored_data['risk_owner_hazard']

    fig = decision_tree(f'{INPUT_ALTERNATIVES}{risk_owner_hazard}.txt', risk_owner_hazard,
                        DIRECTORY_MEASURE_LOGOS + '/colorized', FILTER_CONDITIONS[risk_owner_hazard])
    # figure_identifier = f'assets/figures/decision_tree/alternative_pathways_{relevant_input}.json'
    # with open(figure_identifier, 'r') as f:
    #     fig = pio.from_json(f.read())
    #
    fig, _, _ = scale_figure(fig, viewport)

    return [dcc.Graph(figure=fig, responsive=False)], storage, relevant_input


