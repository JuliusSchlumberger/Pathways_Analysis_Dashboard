import dash
from dash import Input, Output, State
from dashapp import app
from utilities.validate_and_store_data import validate_and_store_data


@app.callback(
    [Output('introduction-validation', 'children'),
     Output('introduction-validation', 'style'),
     Output('impairment-radio-validation', 'style'),
     Output('work-input-validation', 'style'),
     Output('expertise-input-validation', 'style'),
     Output('use_frequency-input-validation', 'style'),
     Output("viztype-input_Stacked_Bar_Chart-validation", 'style'),
     Output("viztype-input_Parallel_Coordinates_Plot-validation", 'style'),
     Output("viztype-input_Heatmap-validation", 'style'),
     Output("viztype-input_Pathways_Map-validation", 'style')],
    [Input('submit-survey-introduction', 'n_clicks')],
    State('storage-general', 'data'),
    prevent_initial_call=True
)
def validate_inputs_on_submit_introduction(submit, stored_data):
    input_ids = [
        'impairment', 'work', 'expertise', 'use_frequency',
        'viztype_barchart', 'viztype_pcp', 'viztype_heatmap', 'viztype_pathways'
    ]
    if submit and submit > 0:
        final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
        final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}
        validation_styles = []
        for input_id in input_ids:
            validation_style, stored_data, final_comment, final_style = validate_and_store_data(
                input_id, stored_data,final_comment, final_style)
            validation_styles.append(validation_style)

        return (final_comment, final_style, *validation_styles)

    return (
        *[dash.no_update] * (len(input_ids) + 2),
    )


@app.callback(
    [Output('alternative_pathways-validation', 'children'),
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
    [Input('submit-survey-alternative_pathways', 'n_clicks')],
    State('storage-general', 'data')
)
def validate_inputs_on_submit_alternative_pathways(submit, stored_data):
    input_ids = [
        'pathway_number', 'f_resilient_crops', 'long_term',
        'flexibility', 'easy', 'confidence', 'enough_information', 'scalability', 'alternative_challenge',
        'alternative_advantage'
    ]
    if submit and submit > 0:
        final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
        print(final_comment)
        final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}
        validation_styles = []
        for input_id in input_ids:
            validation_style, stored_data, final_comment, final_style = validate_and_store_data(
                input_id, stored_data,final_comment, final_style)
            validation_styles.append(validation_style)

        return (final_comment, final_style, *validation_styles)

    return (
        *[dash.no_update] * (len(input_ids) + 2),
    )


@app.callback(
    [Output('pathways_robustness-validation', 'children'),
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
     Output("robustness_advantage-validation", 'style')],
    [Input('submit-survey-pathways-robustness', 'n_clicks')],
    State('storage-general', 'data')
)
def validate_inputs_on_submit_pathways_robustness(submit, stored_data):
    input_ids = [
        'coding', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss',
        'likkert_use-robustness_easy',
        'likkert_use-robustness_confidence',
        'likkert_use-robustness_enough_information', 'likkert_use-robustness_scalability', 'robustness_challenge',
        'robustness_advantage'
    ]

    if submit and submit > 0:
        final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
        final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}
        validation_styles = []

        for input_id in input_ids:
            validation_style, stored_data, final_comment, final_style = validate_and_store_data(
                input_id, stored_data, final_comment, final_style)
            validation_styles.append(validation_style)

        return (final_comment, final_style, *validation_styles)

    return (
        *[dash.no_update] * (len(input_ids) + 2),
    )


@app.callback(
    [Output('pathways_maps-validation', 'children'),
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
     Output("pathways_advantage-validation", 'style')],
    [Input('submit-survey-pathways_maps', 'n_clicks')],
    State('storage-general', 'data')
)
def validate_inputs_on_submit_pathways_maps(submit, stored_data):
    input_ids = [
        'first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift',
        'likkert_use-pathways_maps_easy', 'likkert_use-pathways_maps_confidence',
        'likkert_use-pathways_maps_enough_information', 'likkert_use-pathways_maps_scalability', 'pathways_challenge',
        'pathways_advantage'
    ]

    if submit and submit > 0:
        final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
        final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}
        validation_styles = []

        for input_id in input_ids:
            validation_style, stored_data, final_comment, final_style = validate_and_store_data(
                input_id, stored_data, final_comment, final_style)
            validation_styles.append(validation_style)

        return (final_comment, final_style, *validation_styles)

    return (
        *[dash.no_update] * (len(input_ids) + 2),
    )


# @app.callback(
#     [Output('interaction_effects-validation', 'children'),
#      Output('interaction_effects-validation', 'style'),
#      Output('general_interactions-input-validation', 'style'),
#      Output('interaction_least_productivity_loss-input-validation', 'style'),
#      Output('timing_shifts-input-validation', 'style'),
#      Output('ditch_shift-input-validation', 'style'),
#      Output("likkert_use-interaction_effects_easy-validation", 'style'),
#      Output("likkert_use-interaction_effects_confidence-validation", 'style'),
#      Output("likkert_use-interaction_effects_enough_information-validation", 'style'),
#      Output("likkert_use-interaction_effects_scalability-validation", 'style'),
#      Output("interaction_effects_challenge-validation", 'style'),
#      Output("interaction_effects_advantage-validation", 'style')],
#     [Input('submit-survey-interaction_effects', 'n_clicks')],
#     State('storage-general', 'data')
# )
# def validate_inputs_on_submit_interaction_effects(submit, stored_data):
#     input_ids = [
#         'general_interactions', 'interaction_least_productivity_loss', 'timing_shifts', 'ditch_shift',
#         'likkert_use-interaction_effects_easy', 'likkert_use-interaction_effects_confidence',
#         'likkert_use-interaction_effects_enough_information', 'likkert_use-interaction_effects_scalability',
#         'interaction_effects_challenge', 'interaction_effects_advantage'
#     ]
#
#     if submit and submit > 0:
#         final_comment = "Your responses are saved. You can update your responses by re-submitting. Thank you!"
#         final_style = {'display': 'inline', 'marginLeft': '0.5vw', 'color': '#5cb85c'}
#         validation_styles = []
#
#         for input_id in input_ids:
#             validation_style, stored_data, final_comment, final_style = validate_and_store_data(
#                 input_id, stored_data, final_comment, final_style)
#             validation_styles.append(validation_style)
#
#         return (final_comment, final_style, *validation_styles)
#
#     return (
#         *[dash.no_update] * (len(input_ids) + 2),
#     )
