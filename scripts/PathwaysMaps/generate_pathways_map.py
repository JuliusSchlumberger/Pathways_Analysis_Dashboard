import os
import fnmatch
from scripts.main_central_path_directions import DIRECTORY_PATHWAYS_GENERATOR
from scripts.filter_options import ROBUSTNESS_METRICS_LIST, SCENARIO_OPTIONS
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV, SCENARIOS_INV
from scripts.PathwaysMaps.create_pathways_maps import create_pathways_maps
import pathlib

def find_files_with_string(directory, search_string):
    matching_files = []
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename, f'*{search_string}*'):
            matching_files.append(os.path.join(directory, filename))
    return matching_files

def generate_pathways_map(scenario, risk_owner_hazard, interacting_sector_string=False):
    scenario_str = scenario[0]
    scenarios_title = f'{SCENARIOS_INV[scenario[0]]} climate scenario'

    focus = f'{risk_owner_hazard}_{scenario_str}_average'
    print(focus)
    # focus = foci[1]

    pathlib.Path(f'{DIRECTORY_PATHWAYS_GENERATOR}/processed/').mkdir(parents=True, exist_ok=True)
    planning_horizon = [2020,2120]

    # Initialize Pathways Generator
    line_choice = 'pathways'  # options: 'pathways', 'overlay', 'pathways_and_unique_lines'
    input_with_pathways = True  # True if input file contains pathway numbers
    # optimize_positions = 'both'  # Specifies whether to optimize 'both', 'offset', or 'base_y' positions
    # num_iterations = 'all'  # Number of iterations for optimization, if False, all combinations run
    ylabels = 'logos'  # options: 'logos', 'names', 'numbers'

    # create base figure as png and as plotly
    file_offset = f'{DIRECTORY_PATHWAYS_GENERATOR}/processed/{risk_owner_hazard}_optimized_offset'
    file_base = f'{DIRECTORY_PATHWAYS_GENERATOR}/processed/{risk_owner_hazard}_optimized_base'

    figure_title = f'{ROH_DICT_INV[risk_owner_hazard]} Pathways Map ({scenarios_title})'

    fig = create_pathways_maps(focus, line_choice, input_with_pathways, file_offset, file_base,
                         ylabels, planning_horizon, risk_owner_hazard, figure_title,
                         interaction_identifier=False)

    if interacting_sector_string:
        identifier_for_interactions = f'{DIRECTORY_PATHWAYS_GENERATOR}/interactions/all_sequences_{focus}_{interacting_sector_string}'
        identifier_for_title = identifier_for_interactions.split('&')
        # Initialize Pathways Generator
        line_choice = 'pathways'  # options: 'pathways', 'overlay', 'pathways_and_unique_lines'
        input_with_pathways = True  # True if input file contains pathway numbers
        ylabels = 'logos'  # options: 'logos', 'names', 'numbers'

        figure_title = f'{ROH_DICT_INV[risk_owner_hazard]} Pathways Map ({scenarios_title}; interactions with: {", ".join([ROH_DICT_INV[i] for i in identifier_for_title[1:]])})'

        fig = create_pathways_maps(focus, line_choice, input_with_pathways, file_offset, file_base,
                         ylabels, planning_horizon, risk_owner_hazard, figure_title,
                         interaction_identifier=identifier_for_interactions)

    return fig