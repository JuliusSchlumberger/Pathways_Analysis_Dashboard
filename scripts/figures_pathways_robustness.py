import pandas as pd
import re
import os
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import plotly.io as pio
from scripts.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT,ROH_DICT_INV, SECTOR_OBJECTIVES_BUTTONS, TIMEHORIZONS_INV

from scripts.main_central_path_directions import ROH_LIST
from scripts.map_system_parameters import SECTOR_OBJECTIVES
from scripts.ParallelCoordinates.Parallel_Coordinates_Plot import Parallel_Coordinates_Plot
from scripts.StackedBar.Stacked_Bar_Plot import Stacked_Bar_Plot
from scripts.Heatmap.Heatmap import Heatmap
from scripts.StackedBar.jsonscript_update_legend import UPDATE_LEGEND
from scripts.filter_options import ROBUSTNESS_METRICS_LIST, SCENARIO_OPTIONS
from scripts.helperfunctions.filter_dataframe_for_visualization import filter_dataframe_for_visualization
from scripts.design_choices.main_dashboard_dropdowns import SCENARIOS_INV, ROH_DICT_INV
from scripts.main_central_path_directions import INPUT_ROBUSTNESS_NO_INTERACTION, INPUT_ROBUSTNESS_INTERACTION, INPUT_ROBUSTNESS_MULTIRISK

import pathlib

# Set the option to opt-in to the future behavior
pd.set_option('future.no_silent_downcasting', True)

# Function to extract the identifier from the filename
def extract_identifier(filename):
    match = re.search(r'combi_(.*?)\.', filename)
    if match:
        return match.group(1)
    return None

def pathways_robustness(scenarios, plot_type, risk_owner_hazard, robustness_metric, timehorizon):
    if len(scenarios) == 1:
        scenarios_title = f'{SCENARIOS_INV[scenarios[0]]} climate scenario'
    else:
        better_names = [SCENARIOS_INV[scen] for scen in scenarios]
        scenarios_title = 'across multiple climate scenarios [' + ' & '.join(better_names) + ']'

    figure_title = f'Performance robustness for {ROH_DICT_INV[risk_owner_hazard]} pathways ({timehorizon} years; {scenarios_title})'

    #  Load Data for normal figure
    robustness_path_of_interest = f'{INPUT_ROBUSTNESS_NO_INTERACTION}/robustness_{risk_owner_hazard}_no_interactions.csv'
    robustness_df_of_interest = pd.read_csv(f'{robustness_path_of_interest}')

    if plot_type == 'PCP':
        if robustness_metric in ROBUSTNESS_METRICS_LIST[:-1]:
            relevant_metrics = [robustness_metric]
        else:
            relevant_metrics = [robustness_metric]
    else:
        relevant_metrics = [robustness_metric]

    filtered_df = filter_dataframe_for_visualization(robustness_df_of_interest, risk_owner_hazard,
                                                     timehorizon,
                                                     scenarios,
                                                     relevant_metrics)

    if plot_type == 'PCP':
        fig = Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard, figure_title=figure_title, robustness_metric=robustness_metric)

    elif plot_type == 'StackedBar':
        fig = Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
    elif plot_type == 'Heatmap':
        fig = Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                       sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
    else:
        fig = go.Figure()
    return fig
    # pathlib.Path(f'figures/{plot_type}/{risk_owner_hazard}/').mkdir(parents=True, exist_ok=True)
    # fig.write_json(f'figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{robustness_metric}.json')
    # fig.write_html(
    #     f'Dashboard_v1/assets/figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{robustness_metric}.html')


def pathways_robustness_with_interactions(scenarios, plot_type, risk_owner_hazard, robustness_metric, timehorizon, interacting_sector_string):
    if len(scenarios) == 1:
        scenarios_title = f'{SCENARIOS_INV[scenarios[0]]} climate scenario'
    else:
        better_names = [SCENARIOS_INV[scen] for scen in scenarios]
        scenarios_title = 'across multiple climate scenarios [' + ' & '.join(better_names) + ']'

    #  Load Data for normal figure
    robustness_path_of_interest = f'{INPUT_ROBUSTNESS_NO_INTERACTION}/robustness_{risk_owner_hazard}_no_interactions.csv'
    robustness_df_of_interest = pd.read_csv(f'{robustness_path_of_interest}')

    # Identify files for interaction plots
    identifier_for_interactions = robustness_path_of_interest[:-20].split('/')[-1]  # split off no_interactions.csv
    identifier_for_interactions = f'dynamic_data/data/2_pathways_robustness/interactions/robustness_{risk_owner_hazard}_combi_{interacting_sector_string}.csv'
    if plot_type == 'PCP':
        if robustness_metric in ROBUSTNESS_METRICS_LIST[:-1]:
            # relevant_metrics = ROBUSTNESS_METRICS_LIST[:-1]
            relevant_metrics = [robustness_metric]
        else:
            relevant_metrics = [robustness_metric]
    else:
        relevant_metrics = [robustness_metric]
    filtered_df = filter_dataframe_for_visualization(robustness_df_of_interest, risk_owner_hazard,
                                                     timehorizon,
                                                     scenarios,
                                                     relevant_metrics)

    # identifier = extract_identifier(identifier_for_interactions)
    interaction_df = pd.read_csv(identifier_for_interactions)
    interaction_filtered_df = filter_dataframe_for_visualization(interaction_df,
                                                                 risk_owner_hazard,
                                                                 timehorizon,
                                                                 scenarios,
                                                                 relevant_metrics)
    identifier_for_title = interacting_sector_string.split('&')
    figure_title = f'Performance robustness for {ROH_DICT_INV[identifier_for_title[0]]} pathways ({timehorizon} years; {scenarios_title}; interactions with: {", ".join([ROH_DICT_INV[i] for i in identifier_for_title[1:]])})'

    if plot_type == 'PCP':
        fig = Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                        figure_title=figure_title, robustness_metric=robustness_metric,
                                        df_interaction=interaction_filtered_df)

    elif plot_type == 'StackedBar':
        fig = Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title, df_interaction=interaction_filtered_df)
    elif plot_type == 'Heatmap':
        fig = Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                       sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title, df_interaction=interaction_filtered_df)
    else:
        fig = go.Figure()

    return fig
            # pathlib.Path(f'figures/{plot_type}/{risk_owner_hazard}/').mkdir(parents=True, exist_ok=True)
            # fig.write_json(f'figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{robustness_metric}_combi_{identifier}.json')
