import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.io as pio
import json
from assets.static_inputs import CUSTOM_HOVER
from utilities.scale_figure import scale_figure
from utilities.generate_missing_message import generate_missing_input_message
from scripts.PathwaysMaps.generate_pathways_map import generate_pathways_map
from dashapp import app

@app.callback(
    Output('pathways-graph', 'children'),
    Output('scenarios-maps', 'value'),
    Output('multi_sectoral_interactions_maps', 'value'),
    Output('storage-general', 'data', allow_duplicate=True),
    [Input('url', 'pathname'),
     Input('scenarios-maps', 'value'),
     Input('multi_sectoral_interactions_maps', 'value')],
    [State('storage-general', 'data'),],
    prevent_initial_call=True
)
def update_pathways_graph(pathname, map_scenario, interacting_sectors, stored_data):
    if pathname == '/3-pathways-maps':
        print('pathways', stored_data)
        risk_owner_hazard = stored_data['risk_owner_hazard']

        # Overwrite scenarios if necessary
        if map_scenario != None:
            stored_data['scenarios'] = map_scenario

        ctx = dash.callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if triggered_id == 'multi_sectoral_interactions_maps':
            stored_data['sectoral_interactions_maps'] = interacting_sectors
        else:
            if interacting_sectors is not None:
                stored_data['sectoral_interactions_maps'] = interacting_sectors
            else:
                stored_data['sectoral_interactions_maps'] = 'no_interactions'

        message = generate_missing_input_message(
            ('Climate Scenario', stored_data.get('scenarios', None)))
        print(stored_data['sectoral_interactions_maps'])
        if message:
            return [html.Div('Specify the focus of the analysis (see left), to see a visualization',
                             style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})],dash.no_update, dash.no_update, dash.no_update
        if stored_data.get('sectoral_interactions_maps', None) == None or stored_data.get(
                'sectoral_interactions_maps', None) == 'no_interactions':
            fig = generate_pathways_map([stored_data['scenarios']], risk_owner_hazard, interacting_sector_string=False)
            # figure_identifier = f'assets/figures/PathwaysMaps/{risk_owner_hazard}/pathways_map_{risk_owner_hazard}_{stored_data["scenarios"]}.json'
            interactions = 'no'
        else:
            interactions = 'yes'

            interacting_sector_string = stored_data["risk_owner_hazard"] + '&' + '&'.join(interacting_sectors.split(','))
            fig = generate_pathways_map([stored_data['scenarios']], risk_owner_hazard, interacting_sector_string=interacting_sector_string)
#
        # Read the JSON file and create the Plotly figure
        # with open(figure_identifier, 'r') as f:
        #     fig_dict = json.load(f)
        #     fig = pio.from_json(json.dumps(fig_dict))
        #
        # fig, scaled_height, scaled_width = scale_figure(fig, stored_data)

        # Convert the figure to an HTML string
        fig_html = pio.to_html(fig, full_html=False,  include_plotlyjs='cdn')

        # Custom JavaScript to be added
        custom_js = CUSTOM_HOVER

        # Append the custom JavaScript to the HTML string
        fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"

        # Return the HTML content
        return html.Div([
            html.Iframe(srcDoc=fig_html_with_js,
                        style={"width": "100%",     # Ensure iframe width fills the parent
                        "height": "100%",    # Ensure iframe height fills the parent
                        "border": "none",   # Remove borders if not needed
                        "overflow": "hidden"  # Prevent scrollbars from appearing
                               }
                        )]), stored_data['scenarios'],stored_data['sectoral_interactions_maps'] if interactions == 'yes' else dash.no_update, stored_data
    return dash.no_update, dash.no_update, dash.no_update, stored_data
