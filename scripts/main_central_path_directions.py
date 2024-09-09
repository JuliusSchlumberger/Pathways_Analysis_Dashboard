from scripts.map_system_parameters import MEASURE_NUMBERS
import pandas as pd



# Logos and Legends

DIRECTORY_MEASURE_LOGOS = 'assets/logos/'
LEGENDS_LOCATION = 'assets/legends/'
MARKERS_LOCATION = 'dynamic_data/markers/'

# Input data
INPUTS_ORIGINAL = 'dynamic_data/data/pathways_robustness/'
INPUT_ALTERNATIVES = 'dynamic_data/data/1_alternatives/stage3_portfolios_'
INPUT_ROBUSTNESS_NO_INTERACTION = 'dynamic_data/data/2_pathways_robustness/no_interactions'
INPUT_ROBUSTNESS_INTERACTION = 'dynamic_data/data/2_pathways_robustness/interactions'
INPUT_ROBUSTNESS_MULTIRISK = 'dynamic_data/data/2_pathways_robustness/multi_risk'

INPUT_PATHWAYS_NO_INTERACTION = 'dynamic_data/data/3_pathways_maps/no_interactions'
INPUT_PATHWAYS_INTERACTION = 'dynamic_data/data/3_pathways_maps/interactions'
INPUT_PATHWAYS_MULTIRISK = 'dynamic_data/data/3_pathways_maps/multi_risk'


DIRECTORY_INTERACTIONS = f'dynamic_data/data/pathways_robustness/interactions'
DIRECTORY_PATHWAYS_GENERATOR = 'dynamic_data/data/3_pathways_maps'


ROH_LIST = ['flood_agr', 'drought_agr', 'flood_urb', 'drought_shp']
LIST_COLUMNS = ['climvar', 'pw_combi','objective_parameter','Value','year','scenario_of_interest']
COLUMN_TYPES = {column_name: 'float32' if column_name in ['Value', 'year'] else 'category' for column_name in LIST_COLUMNS}
MEASURE_LOGOS = {measure: f'{DIRECTORY_MEASURE_LOGOS}/{measure}.png' for measure in MEASURE_NUMBERS.keys()}

PATHWYAYS_SPECIFIER = {'flood_agr': 'f_a',
                       'drought_agr': 'd_a',
                       'flood_urb': 'f_u',
                       'drought_shp': 'd_s'}

ALL_PATHWAYS = {'flood_agr': pd.read_csv(f'{INPUT_ALTERNATIVES}flood_agr.txt',
                                          names=['1', '2', '3', '4'], dtype='str'),
                'drought_agr': pd.read_csv(f'{INPUT_ALTERNATIVES}drought_agr.txt',
                                         names=['1', '2', '3', '4'], dtype='str'),
                'flood_urb': pd.read_csv(f'{INPUT_ALTERNATIVES}flood_urb.txt',
                                                         names=['1', '2', '3', '4'], dtype='str'),
                'drought_shp': pd.read_csv(f'{INPUT_ALTERNATIVES}drought_shp.txt',
                                                         names=['1', '2', '3', '4'], dtype='str'),
                }


FILTER_CONDITIONS = {
    ROH_LIST[0]: [0, 1, 3, 5, 7, 9, 11, 13],
    ROH_LIST[1]: [0, 1, 3, 5, 6, 7, 8, 9],
    ROH_LIST[2]: [0, 1, 3, 5, 7, 9, 11, 13],
    ROH_LIST[3]: [0, 1, 2, 4, 5, 7, 8, 9 ],
}



