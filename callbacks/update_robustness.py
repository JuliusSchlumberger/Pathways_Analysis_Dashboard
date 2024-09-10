from dashapp import app
import dash
from dash import dcc, html, Input, Output, State
import plotly.io as pio
from utilities.generate_missing_message import generate_missing_input_message
from utilities.scale_figure import scale_figure
from assets.static_inputs import CUSTOM_LEGEND_CHANGE
from scripts.figures_pathways_robustness import pathways_robustness, pathways_robustness_with_interactions


@app.callback(
    [
        Output('robustness-graph', 'children'),
        Output('timehorizon', 'value', allow_duplicate=True),
        Output('scenarios', 'value', allow_duplicate=True),
        Output('robustness_metric', 'value', allow_duplicate=True),
        Output('options', 'value', allow_duplicate=True),
        Output('multi_sectoral_interactions_robustness', 'value', allow_duplicate=True),
        Output('store-page-C-selection', 'data'),
    ],
    [
        Input('timehorizon', 'value'),
        Input('scenarios', 'value'),
        Input('robustness_metric', 'value'),
        Input('options', 'value'),
        Input('multi_sectoral_interactions_robustness', 'value'),
Input('url', 'pathname'),
    ],
    [State('storage-general', 'data'),
     State('viewport-size', 'data')],
    prevent_initial_call=True
)
def update_robustness_graph(timehorizon, scenarios, robustness_metric, options, interacting_sectors, pathname, stored_data, viewport):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('update_robustness_graph', triggered_id, stored_data)
    if pathname == '/2-pathways-robustness':
        # if any(i is None for i in
        #        [timehorizon, scenarios, robustness_metric, options, interacting_sectors]):
        #     return (dash.no_update, dash.no_update, *[dash.no_update] * 5)

        print('robustness', stored_data)
        # print(timehorizon, scenarios, robustness_metric)
        if timehorizon is not None:
            storage['timehorizon'] = timehorizon
        else:
            storage['timehorizon'] = stored_data.get('timehorizon', None)
        if scenarios is not None:
            print(scenarios)
            storage['scenarios'] = scenarios
        else:
            storage['scenarios'] = stored_data.get('scenarios', None)
        if robustness_metric is not None:
            storage['robustness_metric'] = robustness_metric
        else:
            storage['robustness_metric'] = stored_data.get('robustness_metric', None)
        if options is not None:
            # print(options)
            storage['robustness_plot'] = options
        else:
            storage['robustness_plot'] = stored_data.get('robustness_plot', None)
        if interacting_sectors is not None:
            # print(options)
            storage['interacting_sectors'] = interacting_sectors.split(',')
        else:
            storage['interacting_sectors'] = stored_data.get('interacting_sectors', None)

        message = generate_missing_input_message(
            ('Risk Owner - Hazard Pair', stored_data.get('risk_owner_hazard', None)),
            ('Robustness metric', storage.get('robustness_metric', None)),
            ('Visualization option', storage.get('robustness_plot', None)),
            ('Climate Scenario', storage.get('scenarios', None)))

        if message:
            return html.Div('Specify the focus of the analysis (see left), to see a visualization',
                            style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
                                   'textAlign': 'center'}), *[dash.no_update] * 4, dash.no_update, stored_data

        if storage['interacting_sectors'] == None or storage['interacting_sectors'] == ['no_interactions']:
            # Assume we have necessary details in stored_data to generate the figure
            # file_path = f'assets/figures/{stored_data["robustness_plot"]}/' \
            #             f'{stored_data["risk_owner_hazard"]}/' \
            #             f'plot_{stored_data["timehorizon"]}_{ stored_data["scenarios"]}_{stored_data["robustness_metric"]}.json'
            #
            # with open(file_path, 'r') as f:
            #     fig = pio.from_json(f.read())
            fig = pathways_robustness([storage['scenarios']], storage["robustness_plot"], stored_data['risk_owner_hazard'], storage['robustness_metric'],
                                                  storage['timehorizon'])

            fig, scaled_height, scaled_width = scale_figure(fig, viewport)

            if storage["robustness_plot"] == 'StackedBar':
                # Convert the figure to an HTML string
                fig_html = pio.to_html(fig, full_html=False,  include_plotlyjs='cdn')

                # Custom JavaScript to be added
                custom_js = CUSTOM_LEGEND_CHANGE

                # Append the custom JavaScript to the HTML string
                fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"

                # Return the HTML content
                return (html.Div([
                    html.Iframe(srcDoc=fig_html_with_js,
                                style={"width": f"{scaled_width}px",  # Ensure iframe width fills the parent
                                       "height": f"{scaled_height}px",  # Ensure iframe height fills the parent
                                       "border": "none",  # Remove borders if not needed
                                       "overflow": "hidden"  # Prevent scrollbars from appearing
                                       }
                                )]), storage['timehorizon'], storage['scenarios'],
            storage['robustness_metric'], storage['robustness_plot'], dash.no_update,
                        storage)
            else:
                return ([dcc.Graph(figure=fig, responsive=False, config={
                'displayModeBar': False})], storage['timehorizon'], storage['scenarios'],
                storage['robustness_metric'], storage['robustness_plot'], dash.no_update,
                            storage)


        else:
            interacting_sector_string = stored_data["risk_owner_hazard"] + '&' + '&'.join(storage['interacting_sectors'])
            # file_path = f'assets/figures/{stored_data["robustness_plot"]}/' \
            #                         f'{stored_data["risk_owner_hazard"]}/' \
            #                     f'plot_{stored_data["timehorizon"]}_{ stored_data["scenarios"]}_{stored_data["robustness_metric"]}_combi_{interacting_sector_string}.json'
            #
            # with open(file_path, 'r') as f:
            #     fig = pio.from_json(f.read())

            fig = pathways_robustness_with_interactions([storage['scenarios']], storage["robustness_plot"], stored_data['risk_owner_hazard'], storage['robustness_metric'],
                                                  storage['timehorizon'], interacting_sector_string)

            fig, scaled_height, scaled_width = scale_figure(fig, viewport)

            if storage["robustness_plot"] == 'StackedBar':
                # Convert the figure to an HTML string
                fig_html = pio.to_html(fig, full_html=False,  include_plotlyjs='cdn')

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
                                )]), storage['timehorizon'], storage['scenarios'],
            storage['robustness_metric'], storage['robustness_plot'], storage['interacting_sectors'],
                        storage)
            else:
                return ([dcc.Graph(figure=fig, responsive=False)], storage['timehorizon'], storage['scenarios'],
            storage['robustness_metric'], storage['robustness_plot'], storage['interacting_sectors'],
                        storage)
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
