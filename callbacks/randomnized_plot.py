import dash

from dashapp import app
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT
from scripts.main_central_path_directions import ROH_LIST
from assets.static_inputs import WHICH_OPTIONS
import random


@app.callback(
    Output('storage-general', 'data', allow_duplicate=True),
    Output('options', 'options'),
    Output('options', 'value'),
Output('dynamic-figure-paragraph', 'children'),
    # Output("content", "style"),
    Input("url", "pathname"),
    State('storage-general', 'data'),
    prevent_initial_call=True
)
def update_dropdown_options(pathname, stored_data):
    if pathname == '/2-pathways-robustness':
        if stored_data.get('robustness_plot', None) == None:
            random_key = random.choice(list(WHICH_OPTIONS.keys()))
            # random_key = list(WHICH_OPTIONS.keys())[1]
            # stored_data['robustness_plot'] = WHICH_OPTIONS[random_key]
            stored_data['drop_down_option'] = {random_key: WHICH_OPTIONS[random_key]}

        if stored_data.get('robustness_plot', None) == None:
            fig_description = [
                html.P(
                    f"You need to select a figure type first."
                )
            ]
        elif stored_data.get('robustness_plot', None) == 'PCP':
            fig_description = [html.Div([
                html.P(
                    "In this plot, each pathway corresponds to one polyline spanning a set of parallel axes, one for "
                    "each objective."),
                html.P(
                    "At each parallel axes you can select a range of acceptable values to filter out lines (pathways) "
                    "that do not meet this requirement. Double click on an axis with selected range resets the range."
                )
            ]
            )
            ]
        elif stored_data.get('robustness_plot', None) == 'StackedBar':
            fig_description = [
                html.P(
                    "This figure displays the performance robustness of pathways with regards to multiple "
                    "objectives. The length of the bar represents the performance robustness. A shorter bar, "
                    "represents higher robustness. The length of each colored bar for a given pathway is determined "
                    "relative to the baseline scenario (when no measures are implemented)."
                ),
            ]
        elif stored_data.get('robustness_plot', None) == 'Heatmap':
            fig_description = [
                html.P(
                    "This figure uses colors to highlight relatively better performance robustness across multiple "
                    "objectives (y-axis) of different pathways (y-axis)."
                )
            ]

        return stored_data, stored_data['drop_down_option'], stored_data['robustness_plot'], fig_description  # Return options for page-1
    else:
        return dash.no_update, [], dash.no_update, dash.no_update   # Return empty list if the dropdown isn't rendered (this will be ignored)

