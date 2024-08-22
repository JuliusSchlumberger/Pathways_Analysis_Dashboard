from dash import Input, Output, State
from dashapp import app

@app.callback(
    Output('multi_sectoral_interactions_robustness', 'options'),
    [Input('prev-btn', 'n_clicks'),
     Input('next-btn', 'n_clicks'),
     Input('url', 'pathname')],
    [State('storage-general', 'data')],
    prevent_initial_call=True
)
def set_multi_sector_interaction_options(prev_clicks, next_clicks, path, stored_data):
    return stored_data['interactions']

@app.callback(
    Output('multi_sectoral_interactions_maps', 'options'),
    [Input('prev-btn', 'n_clicks'),
     Input('next-btn', 'n_clicks'),
     Input('url', 'pathname')],
    [State('storage-general', 'data')],
    prevent_initial_call=True
)
def set_multi_sector_interaction_options_maps(prev_clicks, next_clicks, path, stored_data):
    return stored_data['interactions']
