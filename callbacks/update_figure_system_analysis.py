import dash
from dash import html, dcc, callback, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
from dashapp import app
from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT, INTERACTIONS
from scripts.main_central_path_directions import ROH_LIST
from assets.static_inputs import ROH_DICT
from scripts.PathwaysMaps.update_graph_dash import update_graph
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT, ROH_DICT_INV
from scripts.main_central_path_directions import ROH_LIST
from figures_robustness_system_analysis import pathways_robustness_multi_risk
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from utilities.scale_figure import scale_figure







# Callback to update the graph based on selected pathways
@app.callback(
    Output("pathway-graph", "figure", allow_duplicate=True),
    Output('store-page-E-selection', 'data', allow_duplicate=True),
Output("pathway-1", "value", allow_duplicate=True ),
     Output("pathway-2", "value", allow_duplicate=True),
     Output("pathway-3", "value", allow_duplicate=True),
     Output("pathway-4", "value", allow_duplicate=True),
    Output('scenarios', 'value', allow_duplicate=True),
    Output('show_figure_pathways', 'n_clicks', allow_duplicate=True),
    [Input("pathway-1", "value"),
     Input("pathway-2", "value"),
     Input("pathway-3", "value"),
     Input("pathway-4", "value"),
     Input('scenarios', 'value'),
Input('show_figure_pathways', 'n_clicks')
     ],
    State('storage-general', 'data'),
    State('system_analysis_focus', 'value'),
    State('viewport-size', 'data'),
    prevent_initial_call=True
)
def update_graph_fig_pathways(pathway1, pathway2, pathway3, pathway4, scenario, n_clicks, stored_data, focus, viewport):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('create sequence grap', triggered_id)
    if not ctx.triggered:
        return dash.no_update, dash.no_update, *[dash.no_update for i in ROH_LIST], dash.no_update, dash.no_update
    else:
        if focus == 'system_pathways' and n_clicks > 0:
            all_pathways = [pathway1, pathway2, pathway3, pathway4]
            # Create a list of selected pathways, excluding 'not-considered'
            storage['scenarios'] = scenario
            for i, p in enumerate(all_pathways):
                storage[f'pathway_{ROH_LIST[i]}'] = p

            not_considered_count = all_pathways.count('not-considered')
            if not_considered_count <= 2:
                print('this condition is met!')
                fig = update_graph(pathway1, pathway2, pathway3, pathway4, scenario)
                fig, _, _ = scale_figure(fig, viewport)
                return fig, stored_data, pathway1, pathway2, pathway3, pathway4, scenario, 0
            else:
                return dash.no_update, storage, *[storage[f'pathway_{i}'] for i in ROH_LIST], storage['scenarios'], 0
        return dash.no_update, storage, *[storage[f'pathway_{i}'] for i in ROH_LIST], storage[
            'scenarios'], 0

@app.callback(
    Output("performance-graph", "figure"),
    Output('store-page-E-selection', 'data', allow_duplicate=True),
Output("pathway-1", "value", allow_duplicate=True ),
     Output("pathway-2", "value", allow_duplicate=True),
     Output("pathway-3", "value", allow_duplicate=True),
     Output("pathway-4", "value", allow_duplicate=True),
    Output('timehorizon', 'value', allow_duplicate=True),
    Output('scenarios', 'value', allow_duplicate=True),
    Output('robustness_metric', 'value', allow_duplicate=True),
    Output('options', 'value', allow_duplicate=True),
    Output('show_figure_performance', 'n_clicks'),
    [Input("pathway-1", "value"),
     Input("pathway-2", "value"),
     Input("pathway-3", "value"),
     Input("pathway-4", "value"),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('robustness_metric', 'value'),
     Input('options', 'value'),
     Input('show_figure_performance', 'n_clicks')],
    State('storage-general', 'data'),
    State('system_analysis_focus', 'value'),
State('viewport-size', 'data'),
    prevent_initial_call=True
)
def update_graph_fig_robustness(pathway1, pathway2, pathway3, pathway4, timehorizon, scenarios, robustness_metric, options,n_clicks, stored_data, focus, viewport):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('create sequence grap', triggered_id)

    if not ctx.triggered:
        return (dash.no_update, dash.no_update,
             *[dash.no_update for i in ROH_LIST],
             *[dash.no_update] * 4,
             dash.no_update)
    else:
        if focus == 'system_performance' and n_clicks > 0:
            if timehorizon is not None:
                storage['timehorizon'] = timehorizon
            else:
                storage['timehorizon'] = stored_data['timehorizon']
            if scenarios is not None:
                print(scenarios)
                storage['scenarios'] = scenarios
            else:
                storage['scenarios'] = stored_data['scenarios']
            if robustness_metric is not None:
                storage['robustness_metric'] = robustness_metric
            else:
                storage['robustness_metric'] = stored_data['robustness_metric']
            if options is not None:
                # print(options)
                storage['robustness_plot'] = options
            else:
                storage['robustness_plot'] = stored_data['robustness_plot']
            all_pathways = [pathway1, pathway2, pathway3, pathway4]
            for i, p in enumerate(all_pathways):
                storage[f'pathway_{ROH_LIST[i]}'] = p
            print(stored_data)
            # Create a list of selected pathways, excluding 'not-considered'

            print('all_pathways', all_pathways)
            empty_indices = [index for index, sublist in enumerate(all_pathways) if len(sublist) == 0]
            print(empty_indices)

            sectors_of_interest = [ROH_LIST[i] for i in range(len(ROH_LIST)) if i not in empty_indices]
            # # Remove elements from the other list at the identified indices
            # for index in sorted(empty_indices, reverse=True):
            #     del sectors_of_interest[index]
            print(sectors_of_interest)
            if len(sectors_of_interest) < 2:
                return (dash.no_update, storage,
                        *[storage[f'pathway_{i}'] for i in ROH_LIST],
                        *[dash.no_update] * 4,
                        0
                        )
            else:
                pathways_of_interest_dict = {ROH_LIST[i]: all_pathways[i] for i in range(len(all_pathways)) if all_pathways[i] != []}
                print(pathways_of_interest_dict)
                fig = pathways_robustness_multi_risk([scenarios], options, timehorizon, pathways_of_interest_dict,
                                                      sectors_of_interest)
                fig, _, _ = scale_figure(fig, viewport)
                return fig, storage, *[storage[f'pathway_{i}'] for i in ROH_LIST], storage['timehorizon'], \
                storage['scenarios'], storage['robustness_metric'], storage['robustness_plot'], 0

        return (dash.no_update, storage,
                *[dash.no_update for i in ROH_LIST],
                *[dash.no_update] * 4,
                0)
