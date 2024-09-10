from dash.dependencies import Input, Output, State, ALL, MATCH
import dash

from utilities.get_navigation_bar_design import *
from utilities.validate_and_store_data import validate_and_store_data
from dashapp import app, TABLE_NAME
from utilities.validate_and_store_data import validate_and_store_data
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import os
from dash import dcc, html
import dash_bootstrap_components as dbc
from dashapp import app
import json
from assets.static_inputs import PAGES
from pages.A_introduction import layout_A
from pages.B_alternative_pathways import layout_B
from pages.C_pathways_robustness import layout_C
from pages.D_pathways_maps import layout_D
from pages.E_system_analysis import layout_E

DATABASE_URL = os.getenv('DATABASE_URL')

step_content_dict = {
            0: layout_A,
            1: layout_B,
            2: layout_C,
            3: layout_D,
            4: layout_E,
            # 5: layout_F
        }


@app.callback(
    [Output('impairment-radio', 'value'),
     Output('work-input', 'value'),
     Output('expertise-input', 'value', allow_duplicate=True),
     Output('use_frequency-input', 'value'),
     Output("viztype-input_Stacked_Bar_Chart", 'value'),
     Output("viztype-input_Parallel_Coordinates_Plot", 'value'),
     Output("viztype-input_Heatmap", 'value'),
     Output("viztype-input_Pathways_Map", 'value'),
     Output('store-page-A-form', 'data'),
     Output('introduction-validation', 'children'),
     Output('introduction-validation', 'style'),
     Output('impairment-radio-validation', 'style'),
     Output('work-input-validation', 'style'),
     Output('expertise-input-validation', 'style'),
     Output('use_frequency-input-validation', 'style'),
     Output("viztype-input_Stacked_Bar_Chart-validation", 'style'),
     Output("viztype-input_Parallel_Coordinates_Plot-validation", 'style'),
     Output("viztype-input_Heatmap-validation", 'style'),
     Output("viztype-input_Pathways_Map-validation", 'style'),
     ],
    [Input({'type': 'submit-survey', 'index': 1}, 'n_clicks'),
        ],
    [State('impairment-radio', 'value'),
     State('work-input', 'value'),
     State('expertise-input', 'value'),
     State('use_frequency-input', 'value'),
     State("viztype-input_Stacked_Bar_Chart", 'value'),
     State("viztype-input_Parallel_Coordinates_Plot", 'value'),
     State("viztype-input_Heatmap", 'value'),
     State("viztype-input_Pathways_Map", 'value'),
     State('storage-general', 'data')],
    prevent_initial_call=True
)
def handle_introduction_inputs(n_clicks, impairment, work, expertise, use_frequency, viztype_barchart, viztype_pcp,
                                       viztype_heatmap, viztype_pathways, stored_data):

    input_ids = [
        'impairment', 'work', 'expertise', 'use_frequency',
        'viztype_barchart', 'viztype_pcp', 'viztype_heatmap', 'viztype_pathways'
    ]

    storage = {key: stored_data[key] for key in input_ids if key in stored_data}
    storage = {}
    print('introduction_to_store is called', n_clicks)
    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, []) if 'work' in in_id else stored_data.get(in_id, None) for in_id in input_ids],
            storage,
            *[dash.no_update] * (len(input_ids) + 2),
            # False,
            # dash.no_update,
            # *[dash.no_update] * len(PAGES),
            # dash.no_update,
            # False
        )

    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('handle_introduction_inputs - triggered callback:', triggered_id, n_clicks)
    print(f"work-input state: {work}")

    print('introduction_to_store is activated')
    values = [impairment, work, expertise, use_frequency, viztype_barchart, viztype_pcp, viztype_heatmap,
              viztype_pathways]

    validation_styles, storage, final_comment, final_style = validate_and_store_data(
            input_ids, values, storage)
    if final_style['color'] == '#5cb85c':
        storage['completed_introduction'] = 'yes'


        return (
    *[storage.get(in_id, []) if 'work' in in_id else storage.get(in_id, None) for in_id in input_ids],
    storage,
    final_comment, final_style,
    *validation_styles)

    else:
        storage['completed_introduction'] = 'no'
        return (
            *[storage.get(in_id, []) if 'work' in in_id else storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)

@app.callback(
    [
        Output('pathway_number-input', 'value'),
        Output('f_resilient_crops-input', 'value'),
        Output('long_term-input', 'value'),
        Output("flexibility-input", 'value'),
        Output("likkert_use-alternatives_easy", 'value'),
        Output("likkert_use-alternatives_confidence", 'value'),
        Output("likkert_use-alternatives_enough_information", 'value'),
        Output("likkert_use-alternatives_scalability", 'value'),
        Output("alternative_challenge", 'value'),
        Output("alternative_advantage", 'value'),
        Output('store-page-B-form', 'data'),
        Output('alternative_pathways-validation', 'children'),
        Output('alternative_pathways-validation', 'style'),
        Output('pathway_number-input-validation', 'style'),
        Output('f_resilient_crops-input-validation', 'style'),
        Output('long_term-input-validation', 'style'),
        Output("flexibility-input-validation", 'style'),
        Output("likkert_use-alternatives_easy-validation", 'style'),
        Output("likkert_use-alternatives_confidence-validation", 'style'),
        Output("likkert_use-alternatives_enough_information-validation", 'style'),
        Output("likkert_use-alternatives_scalability-validation", 'style'),
        Output("alternative_challenge-validation", 'style'),
        Output("alternative_advantage-validation", 'style'),
    ],
    [
        Input({'type': 'submit-survey', 'index': 2}, 'n_clicks')
    ],
    [
        State('pathway_number-input', 'value'),
        State('f_resilient_crops-input', 'value'),
        State('long_term-input', 'value'),
        State("flexibility-input", 'value'),
        State("likkert_use-alternatives_easy", 'value'),
        State("likkert_use-alternatives_confidence", 'value'),
        State("likkert_use-alternatives_enough_information", 'value'),
        State("likkert_use-alternatives_scalability", 'value'),
        State("alternative_challenge", 'value'),
        State("alternative_advantage", 'value'),
State('storage-general', 'data')
    ],
    prevent_initial_call=True
)
def handle_alternative_pathways(
    n_clicks, pathway_number, f_resilient_crops, long_term, flexibility, easy,
    confidence, enough_information, scalability, alternative_challenge, alternative_advantage, stored_data
):
    storage = {}
    print('alternattive pathways is called')
    input_ids = [
        'pathway_number', 'f_resilient_crops', 'long_term', 'flexibility', 'alternatives_easy',
        'alternatives_confidence', 'alternatives_enough_information', 'alternatives_scalability', 'alternative_challenge', 'alternative_advantage'
    ]

    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            storage,
            *[dash.no_update] * (len(input_ids) + 2)
        )

    # Check if the URL matches the correct page
    print('alternattive pathways is activated')
    values = [
        pathway_number, f_resilient_crops, long_term, flexibility, easy,
        confidence, enough_information, scalability, alternative_challenge, alternative_advantage
    ]

    # Validate and store data
    validation_styles, storage, final_comment, final_style = validate_and_store_data(
        input_ids, values, storage
    )

    # Determine completion status
    if final_style['color'] == '#5cb85c':
        storage['completed_alternative_pathways'] = 'yes'

        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)
    else:
        storage['completed_alternative_pathways'] = 'no'
        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)


@app.callback(
    [
        Output('coding-input', 'value'),
        Output('crop_loss-input', 'value'),
        Output('robustness-input', 'value', allow_duplicate=True),
        Output('tradeoff-input', 'value', allow_duplicate=True),
        Output('general_interactions-input', 'value'),
        Output('interaction_least_productivity_loss-input', 'value', allow_duplicate=True),
        Output("likkert_use-robustness_easy", 'value'),
        Output("likkert_use-robustness_confidence", 'value'),
        Output("likkert_use-robustness_enough_information", 'value'),
        Output("likkert_use-robustness_scalability", 'value'),
        Output("robustness_challenge", 'value'),
        Output("robustness_advantage", 'value'),
        Output('store-page-C-form', 'data'),
        Output('pathways_robustness-validation', 'children'),
        Output('pathways_robustness-validation', 'style'),
        Output('coding-input-validation', 'style'),
        Output('crop_loss-input-validation', 'style'),
        Output('robustness-input-validation', 'style'),
        Output('tradeoff-input-validation', 'style'),
        Output('general_interactions-input-validation', 'style'),
        Output('interaction_least_productivity_loss-input-validation', 'style'),
        Output("likkert_use-robustness_easy-validation", 'style'),
        Output("likkert_use-robustness_confidence-validation", 'style'),
        Output("likkert_use-robustness_enough_information-validation", 'style'),
        Output("likkert_use-robustness_scalability-validation", 'style'),
        Output("robustness_challenge-validation", 'style'),
        Output("robustness_advantage-validation", 'style'),
    ],
    [
        Input({'type': 'submit-survey', 'index': 3}, 'n_clicks'),
    ],
    [
        State('coding-input', 'value'),
        State('crop_loss-input', 'value'),
        State('robustness-input', 'value'),
        State('tradeoff-input', 'value'),
        State('general_interactions-input', 'value'),
        State('interaction_least_productivity_loss-input', 'value'),
        State("likkert_use-robustness_easy", 'value'),
        State("likkert_use-robustness_confidence", 'value'),
        State("likkert_use-robustness_enough_information", 'value'),
        State("likkert_use-robustness_scalability", 'value'),
        State("robustness_challenge", 'value'),
        State("robustness_advantage", 'value'),
State('storage-general', 'data')
    ],
    prevent_initial_call=True
)
def handle_pathways_robustness(n_clicks, coding, crop_loss, robustness, tradeoff, general_interactions,
                               interaction_least_productivity_loss, easy, confidence, enough_information,
                               scalability, robustness_challenge, robustness_advantage, stored_data):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('robustness called', triggered_id)
    input_ids = [
        'coding', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss',
        'robustness_easy', 'robustness_enough_information', 'robustness_enough_informationn',
        'robustness_scalability', 'robustness_challenge', 'robustness_advantage'
    ]

    if n_clicks == 0:
        print('not_relevant')
        return (
            *[stored_data.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else stored_data.get(in_id, None) for in_id in input_ids],
            storage,
            *[dash.no_update] * (len(input_ids) + 2),
        )

    print('robustness activated')
    values = [
        coding, crop_loss, robustness, tradeoff, general_interactions, interaction_least_productivity_loss,
        easy, confidence, enough_information, scalability, robustness_challenge, robustness_advantage
    ]

    validation_styles, storage, final_comment, final_style = validate_and_store_data(
        input_ids, values, storage)
    if final_style['color'] == '#5cb85c':
        storage['completed_pathways_robustness'] = 'yes'


        return (
            *[storage.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)
    else:
        storage['completed_pathways_robustness'] = 'no'
        return (
            *[storage.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles,)

@app.callback(
    [
        Output('first_measure-input', 'value'),
        Output('number_measures-input', 'value'),
        Output('most_flexible15-input', 'value', allow_duplicate=True),
        Output('most_flexible4-input', 'value', allow_duplicate=True),
        Output('timing_shifts-input', 'value'),
        Output('ditch_shift-input', 'value'),
        Output("likkert_use-pathways_maps_easy", 'value'),
        Output("likkert_use-pathways_maps_confidence", 'value'),
        Output("likkert_use-pathways_maps_enough_information", 'value'),
        Output("likkert_use-pathways_maps_scalability", 'value'),
        Output("pathways_challenge", 'value'),
        Output("pathways_advantage", 'value'),
        Output('store-page-D-form', 'data'),
        Output('pathways_maps-validation', 'children'),
        Output('pathways_maps-validation', 'style'),
        Output('first_measure-input-validation', 'style'),
        Output('number_measures-input-validation', 'style'),
        Output('most_flexible15-input-validation', 'style'),
        Output('most_flexible4-input-validation', 'style'),
        Output('timing_shifts-input-validation', 'style'),
        Output('ditch_shift-input-validation', 'style'),
        Output("likkert_use-pathways_maps_easy-validation", 'style'),
        Output("likkert_use-pathways_maps_confidence-validation", 'style'),
        Output("likkert_use-pathways_maps_enough_information-validation", 'style'),
        Output("likkert_use-pathways_maps_scalability-validation", 'style'),
        Output("pathways_challenge-validation", 'style'),
        Output("pathways_advantage-validation", 'style'),
        # Output('end_modal', 'is_open'),
    ],
    [
        Input({'type': 'submit-survey', 'index': 4}, 'n_clicks'),
    ],
    [
        State('first_measure-input', 'value'),
        State('number_measures-input', 'value'),
        State('most_flexible15-input', 'value'),
        State('most_flexible4-input', 'value'),
        State('timing_shifts-input', 'value'),
        State('ditch_shift-input', 'value'),
        State("likkert_use-pathways_maps_easy", 'value'),
        State("likkert_use-pathways_maps_confidence", 'value'),
        State("likkert_use-pathways_maps_enough_information", 'value'),
        State("likkert_use-pathways_maps_scalability", 'value'),
        State("pathways_challenge", 'value'),
        State("pathways_advantage", 'value'),
State('storage-general', 'data')
    ],
    prevent_initial_call=True
)
def handle_pathways_maps(n_clicks, first_measure, number_measures, most_flexible1_5, most_flexible4,
                         timing_shifts, ditch_shift, easy, confidence, enough_information, scalability,
                         pathways_challenge, pathways_advantage, stored_data):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('pathways called', triggered_id)
    input_ids = [
        'first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift',
        'pathways_maps_easy', 'pathways_maps_confidence',
        'pathways_maps_enough_information', 'pathways_maps_scalability', 'pathways_challenge',
        'pathways_advantage'
    ]

    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            storage,
            *[dash.no_update] * (len(input_ids) + 2),
        )

    print('pathways activated')
    values = [
        first_measure, number_measures, most_flexible1_5, most_flexible4, timing_shifts, ditch_shift,
        easy, confidence, enough_information, scalability, pathways_challenge, pathways_advantage
    ]

    validation_styles, storage, final_comment, final_style = validate_and_store_data(
        input_ids, values, storage)
    if final_style['color'] == '#5cb85c':
        storage['completed_pathways_maps'] = 'yes'

        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles
        )

    else:
        storage['completed_pathways_maps'] = 'no'
        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)


@app.callback(
    [
        Output('system_analysis_pathways_1560-input', 'value'),
        Output('system_analysis_pathways_1530-input', 'value'),
        Output('system_analysis_pathways_which_better-input', 'value', allow_duplicate=True),
        Output('system_analysis_performance_1560-input', 'value', allow_duplicate=True),
        Output('system_analysis_performance_1530-input', 'value'),
        Output('system_analysis_performance_which_better-input', 'value'),
        Output("likkert_use-system_analysis_pathways_easy", 'value'),
        Output("likkert_use-system_analysis_performance_easy", 'value'),
        Output("likkert_use-system_analysis_pathways_confidence", 'value'),
        Output("likkert_use-system_analysis_performance_confidence", 'value'),
        Output("likkert_use-system_analysis_pathways_enough_information", 'value'),
        Output("likkert_use-system_analysis_performance_enough_information", 'value'),
Output("likkert_use-system_analysis_pathways_scalability", 'value'),
        Output("likkert_use-system_analysis_performance_scalability", 'value'),
        Output("system_analysis_challenge", 'value'),
        Output("system_analysis_advantage", 'value'),
        Output('store-page-E-form', 'data'),
        Output('system_analysis-validation', 'children'),
        Output('system_analysis-validation', 'style'),
        Output('system_analysis_pathways_1560-input-validation', 'style'),
        Output('system_analysis_pathways_1530-input-validation', 'style'),
        Output('system_analysis_pathways_which_better-input-validation', 'style'),
        Output('system_analysis_performance_1560-input-validation', 'style'),
        Output('system_analysis_performance_1530-input-validation', 'style'),
        Output('system_analysis_performance_which_better-input-validation', 'style'),
        Output("likkert_use-system_analysis_pathways_easy-validation", 'style'),
        Output("likkert_use-system_analysis_performance_easy-validation", 'style'),
        Output("likkert_use-system_analysis_pathways_confidence-validation", 'style'),
        Output("likkert_use-system_analysis_performance_confidence-validation", 'style'),
        Output("likkert_use-system_analysis_pathways_enough_information-validation", 'style'),
        Output("likkert_use-system_analysis_performance_enough_information-validation", 'style'),
        Output("likkert_use-system_analysis_pathways_scalability-validation", 'style'),
        Output("likkert_use-system_analysis_performance_scalability-validation", 'style'),
        Output("system_analysis_challenge-validation", 'style'),
        Output("system_analysis_advantage-validation", 'style'),
    ],
    [
        Input({'type': 'submit-survey', 'index': 5}, 'n_clicks'),
    ],
    [
        State('system_analysis_pathways_1560-input', 'value'),
        State('system_analysis_pathways_1530-input', 'value'),
        State('system_analysis_pathways_which_better-input', 'value'),
        State('system_analysis_performance_1560-input', 'value'),
        State('system_analysis_performance_1530-input', 'value'),
        State('system_analysis_performance_which_better-input', 'value'),
        State("likkert_use-system_analysis_pathways_easy", 'value'),
        State("likkert_use-system_analysis_performance_easy", 'value'),
        State("likkert_use-system_analysis_pathways_confidence", 'value'),
        State("likkert_use-system_analysis_performance_confidence", 'value'),
        State("likkert_use-system_analysis_pathways_enough_information", 'value'),
        State("likkert_use-system_analysis_performance_enough_information", 'value'),
        State("likkert_use-system_analysis_pathways_scalability", 'value'),
        State("likkert_use-system_analysis_performance_scalability", 'value'),
        State("system_analysis_challenge", 'value'),
        State("system_analysis_advantage", 'value'),
State('storage-general', 'data')
    ],
    prevent_initial_call=True
)
def handle_system_analysis(n_clicks, system_analysis_pathways_1560, system_analysis_pathways_1530,
                         system_analysis_pathways_which_better, system_analysis_performance_1560,
                         system_analysis_performance_1530, system_analysis_performance_which_better,
                         system_analysis_pathways_easy, system_analysis_performance_easy,
                         system_analysis_pathways_confidence,
                         system_analysis_performance_confidence, system_analysis_pathways_enough_information,
                         system_analysis_performance_enough_information, system_analysis_pathways_scalability,
                         system_analysis_performance_scalability, system_analysis_challenge, system_analysis_advantage,
                           stored_data):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('system_analysis called', triggered_id)
    input_ids = [
        'system_analysis_pathways_1560', 'system_analysis_pathways_1530', 'system_analysis_pathways_which_better',
        'system_analysis_performance_1560',
        'system_analysis_performance_1530', 'system_analysis_performance_which_better', 'system_analysis_pathways_easy',
        'system_analysis_performance_easy', 'system_analysis_pathways_confidence',
        'system_analysis_performance_confidence', 'system_analysis_pathways_enough_information',
        'system_analysis_performance_enough_information', 'system_analysis_pathways_scalability',
        'system_analysis_performance_scalability', 'system_analysis_challenge', 'system_analysis_advantage',
    ]

    if n_clicks == 0:
        print(f"Returning stored data without click: {storage}")
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            storage,
            *[dash.no_update] * (len(input_ids) + 2),
        )

    print('pathways activated')
    values = [
        system_analysis_pathways_1560, system_analysis_pathways_1530,
        system_analysis_pathways_which_better, system_analysis_performance_1560,
        system_analysis_performance_1530, system_analysis_performance_which_better,
        system_analysis_pathways_easy, system_analysis_performance_easy,
        system_analysis_pathways_confidence,
        system_analysis_performance_confidence, system_analysis_pathways_enough_information,
        system_analysis_performance_enough_information, system_analysis_pathways_scalability,
        system_analysis_performance_scalability, system_analysis_challenge, system_analysis_advantage,
    ]

    validation_styles, storage, final_comment, final_style = validate_and_store_data(
        input_ids, values, storage)
    if final_style['color'] == '#5cb85c':
        storage['completed_system_analysis'] = 'yes'

        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles)

    else:
        storage['completed_system_analysis'] = 'no'
        return (
            *[storage.get(in_id, None) for in_id in input_ids],
            storage,
            final_comment, final_style,
            *validation_styles
        )