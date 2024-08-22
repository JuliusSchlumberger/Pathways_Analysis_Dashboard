from dashapp import app
import dash
from dash import dcc, html, Input, Output, State
import plotly.io as pio
from utilities.generate_missing_message import generate_missing_input_message
from utilities.scale_figure import scale_figure
from assets.static_inputs import CUSTOM_LEGEND_CHANGE


@app.callback(
    [
        Output('robustness-graph', 'children'),
        Output('storage-general', 'data', allow_duplicate=True),
    ],
    [
        Input('timehorizon', 'value'),
        Input('scenarios', 'value'),
        Input('robustness_metric', 'value'),
        Input('options', 'value'),
        Input('multi_sectoral_interactions_robustness', 'value')
    ],
    [State('storage-general', 'data'),
     State('url', 'pathname')],
    prevent_initial_call=True
)
def update_robustness_graph(timehorizon, scenarios, robustness_metric, options, interacting_sectors, stored_data, url):
    if url == '/2-pathways-robustness':
        # print(timehorizon, scenarios, robustness_metric)
        if timehorizon is not None:
            stored_data['timehorizon'] = timehorizon
        if scenarios is not None:
            print(scenarios)
            stored_data['scenarios'] = scenarios
        if robustness_metric is not None:
            stored_data['robustness_metric'] = robustness_metric
        if options is not None:
            # print(options)
            stored_data['robustness_plot'] = options
        # print('options', options)

        ctx = dash.callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if triggered_id == 'multi_sectoral_interactions_robustness':
            print('interactions', interacting_sectors.split(','))
            stored_data['interacting_sectors_robustness'] = interacting_sectors.split(',')
        else:
            if interacting_sectors is not None:
                stored_data['interacting_sectors_robustness'] = interacting_sectors.split(',')
            else:
                stored_data['interacting_sectors_robustness'] = None

        message = generate_missing_input_message(
            ('Risk Owner - Hazard Pair', stored_data.get('risk_owner_hazard', None)),
            ('Robustness metric', stored_data.get('robustness_metric', None)),
            ('Visualization option', stored_data.get('robustness_plot', None)),
            ('Climate Scenario', stored_data.get('scenarios', None)))

        if message:
            return [html.Div('Make Choices (left side of display), to show visualization.',
                             style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})], dash.no_update
        if stored_data.get('interacting_sectors_robustness', None) == None or stored_data.get('interacting_sectors_robustness', None) == ['no_interactions']:
            # Assume we have necessary details in stored_data to generate the figure
            file_path = f'assets/figures/{stored_data["robustness_plot"]}/' \
                        f'{stored_data["risk_owner_hazard"]}/' \
                        f'plot_{stored_data["timehorizon"]}_{ stored_data["scenarios"]}_{stored_data["robustness_metric"]}.json'

            with open(file_path, 'r') as f:
                fig = pio.from_json(f.read())

            fig, _, _ = scale_figure(fig, stored_data)

            return ([dcc.Graph(figure=fig, responsive=False, config={
            'displayModeBar': False})], stored_data)


        else:
            interacting_sector_string = stored_data["risk_owner_hazard"] + '&' + '&'.join(stored_data['interacting_sectors_robustness'])
            print(interacting_sector_string)
            file_path = f'assets/figures/{stored_data["robustness_plot"]}/' \
                                    f'{stored_data["risk_owner_hazard"]}/' \
                                f'plot_{stored_data["timehorizon"]}_{ stored_data["scenarios"]}_{stored_data["robustness_metric"]}_combi_{interacting_sector_string}.json'

            with open(file_path, 'r') as f:
                fig = pio.from_json(f.read())

            fig, scaled_height, scaled_width = scale_figure(fig, stored_data)

            if stored_data["robustness_plot"] == 'StackedBar':
                # Convert the figure to an HTML string
                fig_html = pio.to_html(fig, full_html=False, config={'displayModeBar': False}, include_plotlyjs='cdn')

                # Custom JavaScript to be added
                custom_js = CUSTOM_LEGEND_CHANGE

                # Append the custom JavaScript to the HTML string
                fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"

                # Return the HTML content
                return (html.Div([
                    html.Iframe(srcDoc=fig_html_with_js,
                                style={"width": "100%",  # Ensure iframe width fills the parent
                                       "height": "100%",  # Ensure iframe height fills the parent
                                       "border": "none",  # Remove borders if not needed
                                       "overflow": "hidden"  # Prevent scrollbars from appearing
                                       }
                                )]), stored_data)
            else:
                return ([dcc.Graph(figure=fig, responsive=False, config={
            'displayModeBar': False})], stored_data)

    return dash.no_update, dash.no_update
