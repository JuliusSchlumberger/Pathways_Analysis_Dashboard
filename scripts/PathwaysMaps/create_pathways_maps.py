from scripts.design_choices.main_dashboard_design_choices import MEASURE_COLORS, MAX_X_OFFSET, MAX_Y_OFFSET
from scripts.map_system_parameters import INVERTED_MEASURE_NUMBERS, REPLACING_MEASURE, RENAMING_DICT
from scripts.main_central_path_directions import DIRECTORY_PATHWAYS_GENERATOR

from scripts.PathwaysMaps.pathways_generator_advanced import Pathways_Generator_Advanced

import json


def create_pathways_maps(focus, line_choice, input_with_pathways, optimize_positions, file_offset, file_base,
                         num_iterations, ylabels, savepath, planning_horizon, risk_owner_hazard, figure_title,
                         interaction_identifier=False):
    # Open text file for no interaction file
    file_tipping_points = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_tp_timings_{focus}.txt'
    input_file_with_pathways = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_{focus}.txt'
    file_sequence_only = f'{DIRECTORY_PATHWAYS_GENERATOR}/processed/all_sequences_{focus}_only_sequences.txt'
    print('initiate class: New Pathways Maps')
    NewPathwayMaps = Pathways_Generator_Advanced(
        MEASURE_COLORS, INVERTED_MEASURE_NUMBERS, REPLACING_MEASURE,
        line_choice=line_choice,
        input_with_pathways=input_with_pathways
    )

    with open(f'dynamic_data/data/renamed_pathways/renamed_pathways_{risk_owner_hazard}.json', 'r') as json_file:
        replace_dict = json.load(json_file)
    renaming_dict = {str(v): str(k) for k, v in replace_dict.items()}

    # Create data for no-interaction plot
    print('create start files')
    data = NewPathwayMaps.create_start_files(
        input_file_with_pathways, file_sequence_only, file_tipping_points, renaming_dict, MAX_X_OFFSET, planning_horizon,
    )

    instance_dict, actions, action_transitions, \
    base_y_values, x_offsets, measures_in_pathways, \
    max_instance, base_y_offsets, x_position_dict_ini = data

    if interaction_identifier:
        input_file_with_pathways_with_interaction = f'{DIRECTORY_PATHWAYS_GENERATOR}/interactions/all_sequences_{focus}{interaction_identifier}.txt'
        file_sequence_only_with_interaction = f'{DIRECTORY_PATHWAYS_GENERATOR}/processed/interactions/all_sequences_{focus}{interaction_identifier}_only_sequences.txt'
        file_tipping_points_with_interaction = f'{DIRECTORY_PATHWAYS_GENERATOR}/interactions/all_tp_timings_{focus}{interaction_identifier}.txt'

        # Create data for interaction plot
        print('get start files for interactions')
        interaction_data = NewPathwayMaps.create_start_files(
            input_file_with_pathways_with_interaction,
            file_sequence_only_with_interaction,
            file_tipping_points_with_interaction,
            renaming_dict,
            MAX_X_OFFSET,
            planning_horizon,
            False,   # measures_in_pathways
            base_y_values,
            instance_dict,
            max_instance,
            x_position_dict_ini
        )

        instance_dict, actions_i, action_transitions_i, \
        base_y_values, x_offsets, measures_in_pathways_i, \
        max_instance, base_y_offsets, _ = interaction_data

    # Optimize positions if required
    if optimize_positions:
        if optimize_positions == 'offset':
            with open(f'{file_base}.json', 'r') as file:
                y_values = json.load(file)
        else:
            y_values = base_y_values
        print('optimize positions')
        NewPathwayMaps.optimize_positions(
            instance_dict, actions, action_transitions, y_values,
            max_instance, base_y_offsets, MAX_Y_OFFSET, file_offset, file_base, num_iterations, optimize_positions
        )

    # Load optimized positions
    with open(f'{file_offset}.json', 'r') as file:
        preferred_offset = json.load(file)

    with open(f'{file_base}.json', 'r') as file:
        preferred_base = json.load(file)

    # Create markers
    action_pairs, data, preferred_dict_inv = NewPathwayMaps.create_markers(
        actions, instance_dict, preferred_offset, preferred_base, measures_in_pathways, line_choice
    )
    if interaction_identifier:
        # Create markers with interactions
        action_pairs_i, data_i, preferred_dict_inv = NewPathwayMaps.create_markers(
            actions_i, instance_dict, preferred_offset, preferred_base, measures_in_pathways_i, line_choice
        )
    # Generate and save the base figure without interactions
    if interaction_identifier:
        # fig = NewPathwayMaps.create_base_figure_plotly(
        #     data_i, action_pairs_i, action_transitions_i, x_offsets, preferred_dict_inv,
        #     measures_in_pathways_i, planning_horizon, risk_owner_hazard, figure_title, ylabels=ylabels
        # )
        #
        # # # Write the plot to an HTML file and append custom JavaScript for hover behavior
        # # fig.write_html(f'{filename}.html', include_plotlyjs='cdn')
        # # with open(f'{filename}.html', 'a') as f:
        # #     f.write(HOVER_JS)
        #
        # # Convert the figure to JSON
        # fig_json = fig.to_plotly_json()
        # # Add the custom JavaScript to the JSON structure
        # # fig_json['custom_js'] = HOVER_JS
        #
        # with open(f'{savepath}.json', 'w') as f:
        #     json.dump(fig_json, f)
        #
        # # fig.show()

        fig = NewPathwayMaps.pathways_plotly_with_background(
            data_i, action_pairs_i, action_transitions_i, data, action_pairs, action_transitions, x_offsets, preferred_dict_inv,
            measures_in_pathways_i, measures_in_pathways, planning_horizon, risk_owner_hazard, ylabels, figure_title, color='#d9d9d9'
        )

        # # Write the plot to an HTML file and append custom JavaScript for hover behavior
        # fig.write_html(f'{filename}.html', include_plotlyjs='cdn')
        # with open(f'{filename}.html', 'a') as f:
        #     f.write(HOVER_JS)

        fig_json = fig.to_plotly_json()
        # Add the custom JavaScript to the JSON structure
        # fig_json['custom_js'] = HOVER_JS

        with open(f'{savepath}.json', 'w') as f:
            json.dump(fig_json, f)
    else:
        fig = NewPathwayMaps.create_base_figure_plotly(
            data, action_pairs, action_transitions, x_offsets, preferred_dict_inv,
            measures_in_pathways, planning_horizon, risk_owner_hazard, figure_title, ylabels=ylabels
        )

        # # Write the plot to an HTML file and append custom JavaScript for hover behavior
        # fig.write_html(f'{filename}.html', include_plotlyjs='cdn')
        # with open(f'{filename}.html', 'a') as f:
        #     f.write(HOVER_JS)

        fig_json = fig.to_plotly_json()
        # Add the custom JavaScript to the JSON structure
        # fig_json['custom_js'] = HOVER_JS

        with open(f'{savepath}.json', 'w') as f:
            json.dump(fig_json, f)

