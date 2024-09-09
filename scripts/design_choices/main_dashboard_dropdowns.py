from scripts.map_system_parameters import SECTOR_OBJECTIVES, OBJECTIVE_PARAMETER_DICT, AXIS_LABELS

ROH_DICT = {
    'Farmer - Flood': 'flood_agr',
    'Farmer - Drought': 'drought_agr',
    'Municipality - Flood': 'flood_urb',
    'Ship company - Drought': 'drought_shp',

}

ROH_DICT_INV = {}
for key, element in ROH_DICT.items():
    ROH_DICT_INV[element] = key

TIMEHORIZONS = {
    'next 20 years': 20,
    'next 60 years': 60,
    'next 100 years': 100
}

TIMEHORIZONS_INV = {}
for key, element in TIMEHORIZONS.items():
    TIMEHORIZONS_INV[element] = key

SCENARIOS = {
    'historic': 'D',
    f'1.5 \u2103': 'G',
    f'4 \u2103': 'Wp'
}
SCENARIOS_INV = {}
for key, element in SCENARIOS.items():
    SCENARIOS_INV[element] = key


# PATHWAYS_TO_HIGHLIGHT = {
#     'flood_agr': range(1,13),
#     'drought_agr': range(1,9),
#     'drought_shp': range(1,12),
#     'flood_urb': range(1,18)
# }

PATHWAYS_TO_HIGHLIGHT = {
    'flood_agr': range(1,8),
    'drought_agr': range(1,8),
    'drought_shp': range(1,8),
    'flood_urb': range(1,8)
}

WHICH_OPTIONS = {
    'best': 'best',
    'worst': 'worst'
}

WHICH_OPTIONS = {
    'Parallel Coordinates Plot': 'PCP',
    'Stacked Bar': 'StackedBar',
    'Heatmap': 'Heatmap'
}

ROBUSTNESS_METRICS = {
    '5% confidence interval': '5%',
    '50% confidence interval': '50%',
    '95% confidence interval': '95%',
    'expected robustness': 'average'
}

INTERACTION_VIZ = {
    'Pathways Options': 'image',
    'Pathways Robustness': 'graph'
}

# SECTOR_OBJECTIVES_BUTTONS = {}
# for key in SECTOR_OBJECTIVES:
#     SECTOR_OBJECTIVES_BUTTONS[key]= {}
#     for label in SECTOR_OBJECTIVES[key]:
#         SECTOR_OBJECTIVES_BUTTONS[key][label] = key_item for key_item, value in OBJECTIVE_PARAMETER_DICT.items() if label == value

SECTOR_OBJECTIVES_BUTTONS = {
    key: {label: [key_item for key_item, value in OBJECTIVE_PARAMETER_DICT.items() if label == value]
          for label in labels}
    for key, labels in SECTOR_OBJECTIVES.items()
}

label_keys = list(AXIS_LABELS.keys())
RANGE = {
    AXIS_LABELS[label_keys[0]]: [0,8000],   # Impacted_Lifestock_[#]
    AXIS_LABELS[label_keys[1]]:[0,800], # Farmer_Flood_Measure_Costs_[MEUR]
    AXIS_LABELS[label_keys[2]]:[0,300], # Farmer_Drought_Measure_Costs_[MEUR]
    AXIS_LABELS[label_keys[3]]:[0,100], # Crop_Productivity_Loss_[%]
    AXIS_LABELS[label_keys[4]]:[0,20000], # Impacted_Buildings_[#]
    AXIS_LABELS[label_keys[5]]:[0,1000],    #Municipality_Measure_Costs_[MEUR]
    AXIS_LABELS[label_keys[6]]:[0,2000],   # Delayed_Ships_[#]
    AXIS_LABELS[label_keys[7]]:[0,4000],    # Shipping_Measure_Costs_[MEUR]
    list(ROH_DICT.keys())[0]:[0,7],
    list(ROH_DICT.keys())[1]:[0,7], # 10
    list(ROH_DICT.keys())[2]:[0,7],
    list(ROH_DICT.keys())[3]:[0,7],
    'robustness_metric': [0,1]
}