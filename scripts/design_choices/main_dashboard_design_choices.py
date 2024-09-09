from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


# Define a custom discrete colorscale
# COLORSCALE_HEATMAP = [
#     [0.0, '#fa8de0'], [0.2, '#fa8de0'],  # First segment
#     [0.2, '#f2a7c2'], [0.4, '#f2a7c2'],  # Second segment
#     [0.4, '#f3f3f3'], [0.6, '#f3f3f3'],  # Third segment
#     [0.6, '#d7d57f'], [0.8, '#d7d57f'],  # Fourth segment
#     [0.8, '#c3ea57'], [1.0, '#c3ea57']  # Fifth and last segment
# ]
COLORSCALE_HEATMAP = px.colors.sequential.Greens_r

COLORSCALE = [
    '#fa8de0',  # 0.0 to 0.2
    '#f2a7c2',  # 0.2 to 0.4
    '#f3f3f3',  # 0.4 to 0.6
    '#d7d57f',  # 0.6 to 0.8
    '#c3ea57'   # 0.8 to 1.0
]


# COLORSCALE_PCP = [[0, 'grey'],[.5, 'red'],  [1, 'red']]
COLORSCALE_PCP = [[1000, 'Grey' ]]
COLORSCALE_NAMES = {1000: 'without interactions',}
# COLORSCALE_PCP = [['with interaction', '#c3ea57' ],['without interaction', 'blue'],[.6, 'blue'],['baseline', '#f3f3f3'], [1, '#fa8de0']]
# COLORSCALE_PCP = ['fa8de0', 'f3f3f3', 'f3f3f3', 'c3ea57']

# MEASURE_COLORS = {
#     list(ROH_DICT_INV.keys())[0]: ['#b3cde3', '#6497b1', '#005b96', '#03396c', '#011f4b', '#011a30'],
#     list(ROH_DICT_INV.keys())[1]: ['#ffcc99', '#ffaa66', '#ff8800', '#cc6e00', '#994c00', '#663300'],
#     list(ROH_DICT_INV.keys())[2]: ['#b2dfdb', '#80cbc4', '#4db6ac', '#00897b', '#00695c', '#004d40'],
#     list(ROH_DICT_INV.keys())[3]: ['#cec3e6', '#9d94cc', '#6e63b3', '#4e429f', '#3b318c', '#2e2570']
# }

objectives_cmap = 'plasma'
colorscale = plt.get_cmap(f'{objectives_cmap}')(np.linspace(0, 1, 9))

OBJECTIVE_COLORS = {
    list(ROH_DICT_INV.keys())[0]: [*colorscale[:3]],
    list(ROH_DICT_INV.keys())[1]: [*colorscale[3:5]],
    list(ROH_DICT_INV.keys())[2]: [*colorscale[5:7]],
    list(ROH_DICT_INV.keys())[3]: [*colorscale[7:9]]
}
MEASURE_NUMBERS = {
            'no_measure': 100,
            'd_resilient_crops': 1,
            'd_rain_irrigation': 2,
            'd_gw_irrigation': 3,
            'd_riv_irrigation': 4,
            'd_soilm_practice': 5,
            'd_multimodal_transport': 6,
            'd_medium_ships': 7,
            'd_small_ships': 8,
            'd_dredging': 9,
            'f_resilient_crops': 10,
            'f_ditches': 11,
            'f_local_support': 12,
            'f_dike_elevation_s': 13,
            'f_dike_elevation_l': 14,
            'f_maintenance': 15,
            'f_room_for_river': 16,
            'f_wet_proofing_houses': 17,
            'f_local_protect': 18,
            'f_awareness_campaign': 19
        }
MEASURE_COLORS = {
            '100': 'Grey',
            '0': 'Grey',
            '1': '#ffaa66',
            '2': '#ff8800',
            '3': '#cc6e00',
            '4': '#994c00',
            '5': '#663300',
            '6':'#cec3e6',
            '7': '#9d94cc',
            '8': '#4e429f',
            '9': '#2e2570',
            '10': '#b3cde3',
            '11': '#6497b1',
            '12': '#03396c',
            '13': '#011f4b',
            '14': '#011a30',
            '15': '#005b96',
            '16': '#b2dfdb',
            '17': '#00897b',
            '18': '#00695c',
            '19': '#004d40'
        }


# Generate colors
color_scale = 'viridis'
drought_agr_colors = plt.get_cmap(color_scale)(np.linspace(0.1, .9, 5))
drought_shp_colors = plt.get_cmap(color_scale)(np.linspace(0.1, .9, 4))
flood_agr_colors = plt.get_cmap(color_scale)(np.linspace(0.1, .9, 6))
flood_urb_colors = plt.get_cmap(f'{color_scale}_r')(np.linspace(0.1, .9, 7))

for i in range(1, 6):
    MEASURE_COLORS[str(i)] = mcolors.to_hex(drought_agr_colors[i-1])

for i in range(6, 10):
    MEASURE_COLORS[str(i)] = mcolors.to_hex(drought_shp_colors[i-6])

for i in range(10, 16):
    MEASURE_COLORS[str(i)] = mcolors.to_hex(flood_agr_colors[i - 10])

for i in range(13, 20):
    MEASURE_COLORS[str(i)] = mcolors.to_hex(flood_urb_colors[i-13])

BASE_COLORS_SECTORS = {
    'flood_agr': 'darkviolet',
    'drought_agr': 'violet',
    'flood_urb': 'orangered',
    'drought_shp': 'gold'
}




# Pathways Maps
MAX_X_OFFSET = .7 # will do adjustments in horizontal direction. Needs adjustment if lines of different measures start overlap.
MAX_Y_OFFSET = .48 # will do adjustments in vertical direction between instances. Needs adjustment if markers overlap.

FONTS = {
    "annotations": 12,
    'main': 12,
    'title': 15
}

FIG_DIMENSIONS = {
    'width': 746,
    'height': 467
}

LINE_WIDTH_MARKER = 2
SIZE_MARKER = 12
LINE_WIDTH_LINE = 2
MAX_LINE_OFFSET = 0.2