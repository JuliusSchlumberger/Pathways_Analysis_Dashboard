import textwrap

OBJECTIVE_PARAMETER_DICT = {'DamAgr_f_tot':'Impacted_Lifestock_[#]',
                            'cost_f_a':'Farmer_Flood_Costs_[MEUR]',
                            # 'DamAgr_d_tot':'AgrDrought_DamageReduction', # this is just damage, neglects land loss effect
                            'cost_d_a':'Farmer_Drought_Costs_[MEUR]',
                            'revenue_agr':'Crop_Productivity_Loss_[%]',
                            'DamUrb_tot':'Impacted_Buildings_[#]',
                            'cost_f_u':'Municipality_Costs_[MEUR]',
                            'DamShp_tot':'Delayed_Ships_[#]',
                            'cost_d_s':'Shipping_Costs_[MEUR]'}


AXIS_LABELS = {}
for key, element in OBJECTIVE_PARAMETER_DICT.items():
    AXIS_LABELS[element] = element.replace('_', ' ')


SECTOR_OBJECTIVES = {'flood_agr': [OBJECTIVE_PARAMETER_DICT['cost_f_a'], OBJECTIVE_PARAMETER_DICT['DamAgr_f_tot'], OBJECTIVE_PARAMETER_DICT['revenue_agr'],  ],
                             'drought_agr': [OBJECTIVE_PARAMETER_DICT['revenue_agr'], OBJECTIVE_PARAMETER_DICT['cost_d_a']],
                             'flood_urb': [OBJECTIVE_PARAMETER_DICT['DamUrb_tot'], OBJECTIVE_PARAMETER_DICT['cost_f_u']],
                             'drought_shp': [OBJECTIVE_PARAMETER_DICT['DamShp_tot'], OBJECTIVE_PARAMETER_DICT['cost_d_s']]}

MEASURE_NUMBERS = {
            'no_measure': 0,
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

REPLACING_MEASURE = {   # if measure is not replacing any measure, empty list, else populate the lists
    '0': [],
    '1': ['10'],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': ['1'],
    # blueish group
    '11': [],
    '12': [],
    '13': [],
    '14': [],
    '15': [],
    # greenish group
    '16': [],
    '17': [],
    '18': [],
    '19': [],
}

RENAMING_DICT = {
    'current': '0'
}


INVERTED_MEASURE_NUMBERS = {value: key for key, value in MEASURE_NUMBERS.items()}


method_names = [
    "d_resilient_crops", "d_rain_irrigation", "d_gw_irrigation", "d_riv_irrigation",
    "d_soilm_practice", "d_multimodal_transport", "d_medium_ships", "d_small_ships",
    "d_dredging", "f_resilient_crops", "f_ditches", "f_local_support", "f_dike_elevation_s",
    "f_dike_elevation_l", "f_maintenance", "f_room_for_river", "f_wet_proofing_houses",
    "f_local_protect", "f_awareness_campaign", "no_measure"
]

names = [
    "Drought resilient crops", "Rainwater irrigation", "Groundwater irrigation", "River irrigation",
    "Soil moisture practice", "Multi-modal transport subsidies", "Fleet of medium size ships",
    "Fleet of small size ships", "River dredging", "Flood resilient crops", "Ditch system",
    "Local support conservation scheme", "Small dike elevation increase", "Large dike elevation increase",
    "Dike maintenance", "Room for the River", "Flood proof houses", "Local protection", "Awareness campaign", "No additional measure"
]

# Create dictionary with method_name as keys and Name as values
MEASURE_DICT = dict(zip(method_names, names))

MEASURE_EXPL = {
'no_measure': 'No changes are made to the current system.',
'd_resilient_crops':	'Drought resilient crops are less vulnerable to drought effects by changing the death point and reduction point of the crop',
'd_rain_irrigation':	'Install rainwater collection (over 1% of the agricultural area), storage of a maximum of 20,000m3 of rainwater for the entire area) for irrigation',
'd_gw_irrigation':	'Install groundwater pump to extract a maximum of 0.2m/m2/10days sustainably from a groundwater lens',
'd_riv_irrigation':	'Install pumping capacity (10m3/s) to extract river water (if Q>700) for irrigation purposes',
'd_soilm_practice':	'Adding mulch to the topsoil to increase maximum soil moisture capacity by 25%',
'd_multimodal_transport':	'Negotiate additional contracts to reduce extra shipping costs in case of on-land transport by 15%',
'd_medium_ships':	'Replace shipping fleet with medium size ships',
'd_small_ships':	'Replace shipping fleet with small size ships',
'd_dredging':	'Increase channel depth by a maximum of 1m and repeat the dredging every 15 years',
'f_resilient_crops':	'Flood resilient crops are 10% less vulnerable to flooding and waterlogging',
'f_ditches':	"Increases water run-off and thus reduces the inundation depth by up to 10 cm's",
'f_local_support':	'Initiate campaign to encourage residents hit by a flood to continue to buy (more costly) local crops in the year after a flood',
'f_dike_elevation_s':	'Increase of the current dike crest height by 0.5 m (if dikes are already increased this increase is added)',
'f_dike_elevation_l':	'Increase of the current dike crest height by 1.0 m (if dikes are already increased this increase is added)',
'f_maintenance':	'Improve existing maintenance scheme by sprinkling dikes with river water in case of strong drought and by inspecting the dike to spot any weaknesses (50% discovery rate)',
'f_room_for_river':	'Reduces chances of flooding by widening the channel and changing the Q-h relation',
'f_wet_proofing_houses':	'Make existing houses flood prone, effectively reducing the experienced damage by 10%',
'f_local_protect':	'Install mobile flood protection measures, that protect housing up to an inundation height of 50 cm against any damage',
'f_awareness_campaign':	'Initiate campaign to increase the flood awareness of residents leading to an enhanced damage reduction of up to 20% in the 10 years after a previous flood event',
}


def wrap_text(text, width=80):
    """Wrap text to the specified width."""
    return '<br>'.join(textwrap.wrap(text, width=width))


for key in MEASURE_EXPL.keys():
    MEASURE_EXPL[key] = wrap_text(MEASURE_EXPL[key], width=50)
