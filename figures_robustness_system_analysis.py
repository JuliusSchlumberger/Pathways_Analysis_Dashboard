import pandas as pd
import re
import os
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import plotly.io as pio
from scripts.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT,ROH_DICT_INV, SECTOR_OBJECTIVES_BUTTONS, TIMEHORIZONS_INV
import json
from scripts.main_central_path_directions import ROH_LIST
from scripts.map_system_parameters import SECTOR_OBJECTIVES
from scripts.ParallelCoordinates.PCP_multi_risk import Parallel_Coordinates_Plot
from scripts.StackedBar.StackedBar_multi_risk import Stacked_Bar_Plot
from scripts.Heatmap.Heatmap_multi_risk import Heatmap
from scripts.StackedBar.jsonscript_update_legend import UPDATE_LEGEND
from scripts.filter_options import ROBUSTNESS_METRICS_LIST, SCENARIO_OPTIONS
from scripts.helperfunctions.filter_dataframe_for_visualization import filter_dataframe_for_visualization
from scripts.design_choices.main_dashboard_dropdowns import SCENARIOS_INV, ROH_DICT_INV
from scripts.main_central_path_directions import INPUT_ROBUSTNESS_NO_INTERACTION, INPUT_ROBUSTNESS_INTERACTION, INPUT_ROBUSTNESS_MULTIRISK

import pathlib
# Set the option to opt-in to the future behavior
pd.set_option('future.no_silent_downcasting', True)

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



# Function to extract the identifier from the filename
def extract_identifier(filename):
    match = re.search(r'combi_(.*?)\.', filename)
    if match:
        return match.group(1)
    return None


def pathways_robustness_multi_risk(scenarios, plot_type, timehorizon, pathways_of_interest_dict,
                                   sectors_of_interest_list, robustness_metric='average'):
    # sectors of interest must follow the same order as the general naming convention f_a, d_a, f_u, d_s
    scenarios_title = f'{SCENARIOS_INV[scenarios[0]]} climate scenario'
    print(pathways_of_interest_dict)
    print(sectors_of_interest_list)
    #  Load Data for normal figure
    df_list = []
    for sector in sectors_of_interest_list:
        other_sectors = [s for s in sectors_of_interest_list if s != sector]
        pathname = f'{INPUT_ROBUSTNESS_MULTIRISK}/robustness_{sector}_combi_{sector}&{"&".join(other_sectors)}.csv'
        sector_focus = pd.read_csv(f'{pathname}')
        filtered_df = filter_dataframe_for_visualization(sector_focus, sector,timehorizon,scenarios, [robustness_metric], sector_focus=pathways_of_interest_dict)
        df_list.append(filtered_df)

    relevant_pathways_objectives_df = pd.concat(df_list, ignore_index=True)

    for risk_owner_hazard in pathways_of_interest_dict:
        with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
            replace_dict = json.load(json_file)
        invert_replace_dict = {v: int(k) for k, v in replace_dict.items()}
        # print(error)
        # Replace old values with new values in the 'risk_owner_hazard' column
        relevant_pathways_objectives_df[risk_owner_hazard] = relevant_pathways_objectives_df[
            risk_owner_hazard].replace(invert_replace_dict)

    relevant_pathways_objectives_df['pw_combi'] = relevant_pathways_objectives_df.apply(lambda row: '_'.join([str(row[risk_owner_hazard]) for risk_owner_hazard in ROH_LIST]),
                              axis=1)

    relevant_pathways_objectives_df = relevant_pathways_objectives_df[
         (pd.concat([relevant_pathways_objectives_df[key].isin(value) for key, value in pathways_of_interest_dict.items()], axis=1).all(axis=1))
        ].copy()

    figure_title = f'Performance robustness across {", ".join([ROH_DICT_INV[s] for s in sectors_of_interest_list])} for selected pathways ({timehorizon} years; {scenarios_title})'
    if plot_type == 'PCP':
        fig = Parallel_Coordinates_Plot(df=relevant_pathways_objectives_df, sectors_of_interest_list=sectors_of_interest_list,
                                        figure_title=figure_title, robustness_metric=robustness_metric)
    #
    elif plot_type == 'StackedBar':
        fig = Stacked_Bar_Plot(df=relevant_pathways_objectives_df, sectors_of_interest_list=sectors_of_interest_list,
                                figure_title=figure_title)
    elif plot_type == 'Heatmap':
        fig = Heatmap(df=relevant_pathways_objectives_df, sectors_of_interest_list=sectors_of_interest_list,
                       figure_title=figure_title)
    else:
        fig = go.Figure()
    return fig
    #
    #         pathlib.Path(f'figures/{plot_type}/{risk_owner_hazard}/').mkdir(parents=True, exist_ok=True)
    #         fig.write_json(f'figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{robustness_metric}_combi_{identifier}.json')


# for plot_type in ['StackedBar', 'PCP', 'Heatmap']:
# pathways_of_interest_dict = {
#     'flood_agr': [13, 7],
#     'drought_agr': [1, 5],
#     'drought_shp': [1, 2],
#     'flood_urb': [1, 3],
# }
#
# sectors_of_interest = ['flood_agr', 'drought_agr','flood_urb', 'drought_shp']
# sectors_of_interest = ['flood_agr','drought_agr', 'flood_urb']


# No Interactions
# for plot_type in ['StackedBar']:
#     # for risk_owner_hazard in ROH_DICT_INV:
#     for risk_owner_hazard in ['flood_agr']:
#         for robustness_metric in ROBUSTNESS_METRICS_LIST:
#             for timehorizon in TIMEHORIZONS_INV:
#                 # for timehorizon in {100: 'next 100 years'}:
#                 for scenarios in SCENARIO_OPTIONS:
#                     # for scenarios in [['Wp']]:
#                     print(plot_type, risk_owner_hazard, robustness_metric, timehorizon, scenarios)
#                     if len(scenarios) > 1:
#                         scenario_str = '&'.join(scenarios)
#                     else:
#                         scenario_str = scenarios[0]
#                     pathways_robustness_multi_risk(scenarios, plot_type, timehorizon, pathways_of_interest_dict, sectors_of_interest)
#



