import dash
from dash import Input, Output, State
from dashapp import app

@app.callback(
    [Output('impairment-radio', 'value'),
     Output('work-input', 'value'),
     Output('expertise-input', 'value'),
     Output('use_frequency-input', 'value'),
     Output("viztype-input_Stacked_Bar_Chart", 'value'),
     Output("viztype-input_Parallel_Coordinates_Plot", 'value'),
     Output("viztype-input_Heatmap", 'value'),
     Output("viztype-input_Pathways_Map", 'value'),
     Output('storage-general', 'data', allow_duplicate=True)],
    [Input('impairment-radio', 'value'),
     Input('work-input', 'value'),
     Input('expertise-input', 'value'),
     Input('use_frequency-input', 'value'),
     Input("viztype-input_Stacked_Bar_Chart", 'value'),
     Input("viztype-input_Parallel_Coordinates_Plot", 'value'),
     Input("viztype-input_Heatmap", 'value'),
     Input("viztype-input_Pathways_Map", 'value'),],
    State('storage-general', 'data'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def update_stored_data_on_change_introduction(impairment, work, expertise, use_frequency, viztype_barchart, viztype_pcp,
                                       viztype_heatmap, viztype_pathways, stored_data, url, ):
    input_ids = [
        'impairment', 'work', 'expertise', 'use_frequency',
        'viztype_barchart', 'viztype_pcp', 'viztype_heatmap', 'viztype_pathways'
    ]

    if url == '/0-introduction':
        input_ids = [
            'impairment', 'work', 'expertise', 'use_frequency',
            'viztype_barchart', 'viztype_pcp', 'viztype_heatmap', 'viztype_pathways'
        ]
        values = [impairment, work, expertise, use_frequency, viztype_barchart, viztype_pcp, viztype_heatmap,
                  viztype_pathways]

        for input_id, value in zip(input_ids, values):
            if value is not None:
                stored_data[input_id] = value
        print('introduction', stored_data)
        print(*[stored_data.get(in_id, None) for in_id in input_ids])
        # Populate input fields with stored values when the URL matches a certain path
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data
        )

    # Otherwise, just return the updated stored data
    return (
        *[dash.no_update] * len(input_ids),
        stored_data
    )


@app.callback(
    [Output('pathway_number-input', 'value'),
     Output('f_resilient_crops-input', 'value'),
     Output('long_term-input', 'value'),
     Output("flexibility-input", 'value'),
     Output("likkert_use-alternatives_easy", 'value'),
     Output("likkert_use-alternatives_confidence", 'value'),
     Output("likkert_use-alternatives_enough_information", 'value'),
     Output("likkert_use-alternatives_scalability", 'value'),
     Output("alternative_challenge", 'value'),
     Output("alternative_advantage", 'value'),
     Output('storage-general', 'data', allow_duplicate=True)],
    [Input('pathway_number-input', 'value'),
     Input('f_resilient_crops-input', 'value'),
     Input('long_term-input', 'value'),
     Input("flexibility-input", 'value'),
     Input("likkert_use-alternatives_easy", 'value'),
     Input("likkert_use-alternatives_confidence", 'value'),
     Input("likkert_use-alternatives_enough_information", 'value'),
     Input("likkert_use-alternatives_scalability", 'value'),
    Input("alternative_challenge", 'value'),
     Input("alternative_advantage", 'value'),
     ],
    State('storage-general', 'data'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def update_stored_data_on_change_alternatives(pathway_number, f_resilient_crops, long_term, flexibility, easy,
                                       confidence, enough_information, scalability, alternative_challenge, alternative_advantage, stored_data, url):
    input_ids = [
        'pathway_number', 'f_resilient_crops', 'long_term',
        'flexibility', 'easy', 'confidence', 'enough_information', 'scalability', 'alternative_challenge', 'alternative_advantage'
    ]
    if url == '/1-measure-sequences':
        values = [pathway_number, f_resilient_crops, long_term, flexibility, easy, confidence,
                enough_information, scalability, alternative_challenge, alternative_advantage]

        for input_id, value in zip(input_ids, values):
            if value is not None:
                stored_data[input_id] = value
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data
        )

    # Otherwise, just return the updated stored data
    return (
        *[dash.no_update] * len(input_ids),
        stored_data
    )

@app.callback(
    [
        Output('coding-input', 'value'),
        Output('crop_loss-input', 'value'),
        Output('robustness-input', 'value'),
        Output('tradeoff-input', 'value'),
        Output('general_interactions-input', 'value'),
        Output('interaction_least_productivity_loss-input', 'value'),
        Output("likkert_use-robustness_easy", 'value'),
        Output("likkert_use-robustness_confidence", 'value'),
        Output("likkert_use-robustness_enough_information", 'value'),
        Output("likkert_use-robustness_scalability", 'value'),
        Output("robustness_challenge", 'value'),
        Output("robustness_advantage", 'value'),
        Output('timehorizon', 'value'),
        Output('scenarios', 'value'),
        Output('robustness_metric', 'value'),
        Output('options', 'value', allow_duplicate=True),
        Output('multi_sectoral_interactions_robustness', 'value', allow_duplicate=True),
        Output('storage-general', 'data', allow_duplicate=True)
    ],
    [
        Input('coding-input', 'value'),
        Input('crop_loss-input', 'value'),
        Input('robustness-input', 'value'),
        Input('tradeoff-input', 'value'),
        Input('general_interactions-input', 'value'),
        Input('interaction_least_productivity_loss-input', 'value'),
        Input("likkert_use-robustness_easy", 'value'),
        Input("likkert_use-robustness_confidence", 'value'),
        Input("likkert_use-robustness_enough_information", 'value'),
        Input("likkert_use-robustness_scalability", 'value'),
        Input("robustness_challenge", 'value'),
        Input("robustness_advantage", 'value'),
        Input('timehorizon', 'value'),
        Input('scenarios', 'value'),
        Input('robustness_metric', 'value'),
        Input('options', 'value'),
        Input('multi_sectoral_interactions_robustness', 'value')
    ],
    State('storage-general', 'data'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def update_stored_data_on_change_robustness(
    coding, crop_loss, robustness, tradeoff, general_interactions, interaction_least_productivity_loss, easy, confidence,
    enough_information, scalability, robustness_challenge, robustness_advantage,
    timehorizon, scenarios, robustness_metric, options, multi_sectoral_interactions,
    stored_data, url
):
    input_ids = [
        'coding', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss',
        'likkert_use-robustness_easy',
        'likkert_use-robustness_confidence', 'likkert_use-robustness_enough_information',
        'likkert_use-robustness_scalability', 'robustness_challenge', 'robustness_advantage',
        'timehorizon', 'scenarios', 'robustness_metric', 'options', 'multi_sectoral_interactions'
    ]

    if url == '/2-pathways-robustness':
        values = [
            coding, crop_loss, robustness, tradeoff, general_interactions, interaction_least_productivity_loss,
            easy, confidence,
            enough_information, scalability, robustness_challenge, robustness_advantage,
            timehorizon, scenarios, robustness_metric, options, multi_sectoral_interactions
        ]

        for input_id, value in zip(input_ids, values):
            if value is not None:
                stored_data[input_id] = value
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data
        )

    # Otherwise, just return the updated stored data
    return (
        *[dash.no_update] * len(input_ids),
        stored_data
    )


@app.callback(
    [Output('first_measure-input', 'value'),
     Output('number_measures-input', 'value'),
     Output('most_flexible15-input', 'value'),
     Output('most_flexible4-input', 'value'),
     Output('timing_shifts-input', 'value'),
     Output('ditch_shift-input', 'value'),
     Output("likkert_use-pathways_maps_easy", 'value'),
     Output("likkert_use-pathways_maps_confidence", 'value'),
     Output("likkert_use-pathways_maps_enough_information", 'value'),
     Output("likkert_use-pathways_maps_scalability", 'value'),
     Output("pathways_challenge", 'value'),
     Output("pathways_advantage", 'value'),
     Output('scenario-maps', 'value'),
     Output('multi_sectoral_interactions_maps', 'value'),
     Output('storage-general', 'data', allow_duplicate=True)],
    [Input('first_measure-input', 'value'),
     Input('number_measures-input', 'value'),
     Input('most_flexible15-input', 'value'),
     Input('most_flexible4-input', 'value'),
     Input('timing_shifts-input', 'value'),
     Input('ditch_shift-input', 'value'),
     Input("likkert_use-pathways_maps_easy", 'value'),
     Input("likkert_use-pathways_maps_confidence", 'value'),
     Input("likkert_use-pathways_maps_enough_information", 'value'),
     Input("likkert_use-pathways_maps_scalability", 'value'),
     Input("pathways_challenge", 'value'),
     Input("pathways_advantage", 'value'),
     Input('scenario-maps', 'value'),
     Input('multi_sectoral_interactions_maps', 'value'),
     ],
    State('storage-general', 'data'),
    State('url', 'pathname'),
    prevent_initial_call=True
)
def update_stored_data_on_change_pathways_maps(first_measure, number_measures, most_flexible1_5, most_flexible4,
                                               timing_shifts, ditch_shift, easy,
                                               confidence, enough_information, scalability, pathways_challenge,
                                               pathways_advantage, scenario, sectoral_interactions,  stored_data, url,):
    input_ids = [
        'first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift',
        'likkert_use-pathways_maps_easy', 'likkert_use-pathways_maps_confidence',
        'likkert_use-pathways_maps_enough_information', 'likkert_use-pathways_maps_scalability', 'pathways_challenge',
        'pathways_advantage', 'scenario-maps', 'multi_sectoral_interactions_maps'
    ]

    if url == '/3-pathways-maps':
        values = [first_measure, number_measures, most_flexible1_5, most_flexible4, timing_shifts, ditch_shift,
                  easy, confidence,
                  enough_information, scalability, pathways_challenge, pathways_advantage, scenario, sectoral_interactions]

        for input_id, value in zip(input_ids, values):
            if value is not None:
                stored_data[input_id] = value
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data
        )

    # Otherwise, just return the updated stored data
    return (
        *[dash.no_update] * len(input_ids),
        stored_data
    )
#
# @app.callback(
#     [Output('general_interactions-input', 'value'),
#      Output('interaction_least_productivity_loss-input', 'value'),
#      Output('timing_shifts-input', 'value'),
#      Output('ditch_shift-input', 'value'),
#      Output("likkert_use-interaction_effects_easy", 'value'),
#      Output("likkert_use-interaction_effects_confidence", 'value'),
#      Output("likkert_use-interaction_effects_enough_information", 'value'),
#      Output("likkert_use-interaction_effects_scalability", 'value'),
#      Output("interaction_effects_challenge", 'value'),
#      Output("interaction_effects_advantage", 'value'),
#      Output('storage-general', 'data', allow_duplicate=True)],
#     [Input('general_interactions-input', 'value'),
#      Input('interaction_least_productivity_loss-input', 'value'),
#      Input('timing_shifts-input', 'value'),
#      Input('ditch_shift-input', 'value'),
#      Input("likkert_use-interaction_effects_easy", 'value'),
#      Input("likkert_use-interaction_effects_confidence", 'value'),
#      Input("likkert_use-interaction_effects_enough_information", 'value'),
#      Input("likkert_use-interaction_effects_scalability", 'value'),
#      Input("interaction_effects_challenge", 'value'),
#      Input("interaction_effects_advantage", 'value'),],
#     State('storage-general', 'data'),
#     State('url', 'pathname'),
#     prevent_initial_call=True
# )
# def update_stored_data_on_change_interaction_effects(general_interactions, interaction_least_productivity_loss, timing_shifts, ditch_shift, easy,
#                                                      confidence, enough_information, scalability, interaction_effects_challenge,
#                                                      interaction_effects_advantage, stored_data, url):
#     input_ids = [
#         'general_interactions', 'interaction_least_productivity_loss', 'timing_shifts', 'ditch_shift',
#         'likkert_use-interaction_effects_easy', 'likkert_use-interaction_effects_confidence',
#         'likkert_use-interaction_effects_enough_information', 'likkert_use-interaction_effects_scalability',
#         'interaction_effects_challenge', 'interaction_effects_advantage'
#     ]
#
#
#     if url == '/interaction-effects':
#         values = [general_interactions, interaction_least_productivity_loss, timing_shifts, ditch_shift, easy,
#                   confidence,
#                   enough_information, scalability, interaction_effects_challenge, interaction_effects_advantage]
#
#         for input_id, value in zip(input_ids, values):
#             if value is not None:
#                 stored_data[input_id] = value
#         return (
#             *[stored_data.get(in_id, None) for in_id in input_ids],
#             stored_data
#         )
#
#     # Otherwise, just return the updated stored data
#     return (
#         *[dash.no_update] * len(input_ids),
#         stored_data
#     )
