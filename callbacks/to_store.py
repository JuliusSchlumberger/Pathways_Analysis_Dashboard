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
from pages.F_multi_risk_pathways import layout_F

DATABASE_URL = os.getenv('DATABASE_URL')

step_content_dict = {
            0: layout_A,
            1: layout_B,
            2: layout_C,
            3: layout_D,
            # 4: layout_E,
            # 5: layout_F
        }


def save_response_to_db(DATABASE_URL, user_id, data):
    # Adjust the URL format if necessary
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    # Set up SQLAlchemy
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    class SurveyResponse(Base):
        __tablename__ = TABLE_NAME
        id = Column(Integer, primary_key=True)
        user_id = Column(String)
        data = Column(Text)

    session = Session()
    response = session.query(SurveyResponse).filter_by(user_id=user_id).first()
    if response:
        response.data = json.dumps(data)
    else:
        response = SurveyResponse(user_id=user_id, data=json.dumps(data))
        session.add(response)
    session.commit()
    session.close()
#

# Assume validate_and_store_data and save_response_to_db functions are already defined as you shared earlier.

@app.callback(
    Output('dummy-output', 'children', allow_duplicate=True),
    Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks'),
    State('storage-general', 'data'),
    prevent_initial_call=True
)
def update_store_complete(n_clicks, stored_data):
    # Only update the store when the survey is complete and submit button is clicked
    if n_clicks:
        try:
            save_response_to_db(DATABASE_URL, stored_data['existing_id'], stored_data)
        except Exception as e:
            print(f"Error storing data: {e}")
        return True
    return False


@app.callback(
    [Output('impairment-radio', 'value'),
     Output('work-input', 'value'),
     Output('expertise-input', 'value', allow_duplicate=True),
     Output('use_frequency-input', 'value'),
     Output("viztype-input_Stacked_Bar_Chart", 'value'),
     Output("viztype-input_Parallel_Coordinates_Plot", 'value'),
     Output("viztype-input_Heatmap", 'value'),
     Output("viztype-input_Pathways_Map", 'value'),
     Output('storage-general', 'data', allow_duplicate=True),
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
     Output('to_store-complete', 'data', allow_duplicate=True),
     Output('page-content', 'children', allow_duplicate=True),
        *[Output(f"step-{i}-link", "children", allow_duplicate=True) for i in range(len(PAGES))],
        Output('url', 'pathname', allow_duplicate=True),
        Output("progress_modal", "is_open", allow_duplicate=True),
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
    print('introduction_to_store is called')
    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, []) if 'work' in in_id else stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            *[dash.no_update] * (len(input_ids) + 2),
            False,
            dash.no_update,
            *[dash.no_update] * len(PAGES),
            dash.no_update,
            False
        )

    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('handle_introduction_inputs - triggered callback:', triggered_id, n_clicks)
    print(f"work-input state: {work}")

    print('introduction_to_store is activated')
    values = [impairment, work, expertise, use_frequency, viztype_barchart, viztype_pcp, viztype_heatmap,
              viztype_pathways]

    validation_styles, stored_data, final_comment, final_style = validate_and_store_data(
            input_ids, values, stored_data)
    if final_style['color'] == '#5cb85c':
        stored_data['completed_introduction'] = 'yes'
        current_step = get_step_from_pathname(stored_data['current_url'])
        new_step = min(current_step + 1, len(PAGES) - 1)
        to_store_complete = True

        new_url = PAGES[new_step]['url']
        stored_data['current_url'] = new_url

        # Select the correct layout based on the new step
        content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(new_step)

        return (
    *[stored_data.get(in_id, []) if 'work' in in_id else stored_data.get(in_id, None) for in_id in input_ids],
    stored_data,
    final_comment, final_style,
    *validation_styles, to_store_complete,
            content, *page_names, stored_data['current_url'], False)

    else:
        stored_data['completed_introduction'] = 'no'
        to_store_complete = False
        return (
            *[stored_data.get(in_id, []) if 'work' in in_id else stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            dash.no_update, *[dash.no_update] * len(
            PAGES), dash.no_update, True)

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
        Output('storage-general', 'data', allow_duplicate=True),
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
        Output('to_store-complete', 'data', allow_duplicate=True),
        Output('page-content', 'children', allow_duplicate=True),
        *[Output(f"step-{i}-link", "children", allow_duplicate=True) for i in range(len(PAGES))],
        Output('url', 'pathname', allow_duplicate=True),
        Output("progress_modal", "is_open", allow_duplicate=True),
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
        State('storage-general', 'data'),
        State('url', 'pathname')
    ],
    prevent_initial_call=True
)
def handle_alternative_pathways(
    n_clicks, pathway_number, f_resilient_crops, long_term, flexibility, easy,
    confidence, enough_information, scalability, alternative_challenge, alternative_advantage, stored_data, url
):
    print('alternattive pathways is called')
    input_ids = [
        'pathway_number', 'f_resilient_crops', 'long_term', 'flexibility', 'easy',
        'confidence', 'enough_information', 'scalability', 'alternative_challenge', 'alternative_advantage'
    ]

    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            *[dash.no_update] * (len(input_ids) + 2),
            False,
            dash.no_update,
            *[dash.no_update] * len(PAGES),
            dash.no_update,
            False
        )

    # Check if the URL matches the correct page
    print('alternattive pathways is activated')
    values = [
        pathway_number, f_resilient_crops, long_term, flexibility, easy,
        confidence, enough_information, scalability, alternative_challenge, alternative_advantage
    ]

    # Validate and store data
    validation_styles, stored_data, final_comment, final_style = validate_and_store_data(
        input_ids, values, stored_data
    )

    # Determine completion status
    if final_style['color'] == '#5cb85c':
        stored_data['completed_alternative_pathways'] = 'yes'
        current_step = get_step_from_pathname(stored_data['current_url'])
        new_step = min(current_step + 1, len(PAGES) - 1)
        to_store_complete = True

        new_url = PAGES[new_step]['url']
        stored_data['current_url'] = new_url

        # Select the correct layout based on the new step
        content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(new_step)

        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            content, *page_names, stored_data['current_url'], False)
    else:
        stored_data['completed_alternative_pathways'] = 'no'
        to_store_complete = False
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, True)


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
        Output('storage-general', 'data', allow_duplicate=True),
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
        Output('to_store-complete', 'data', allow_duplicate=True),
        Output('page-content', 'children', allow_duplicate=True),
        *[Output(f"step-{i}-link", "children", allow_duplicate=True) for i in range(len(PAGES))],
        Output('url', 'pathname', allow_duplicate=True),
        Output("progress_modal", "is_open", allow_duplicate=True),
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
        State('storage-general', 'data'),
        State('url', 'pathname')
    ],
    prevent_initial_call=True
)
def handle_pathways_robustness(n_clicks, coding, crop_loss, robustness, tradeoff, general_interactions,
                               interaction_least_productivity_loss, easy, confidence, enough_information,
                               scalability, robustness_challenge, robustness_advantage, stored_data, url):
    print('robustness called')
    input_ids = [
        'coding', 'crop_loss', 'robustness', 'tradeoff', 'general_interactions', 'interaction_least_productivity_loss',
        'likkert_use-robustness_easy', 'likkert_use-robustness_confidence', 'likkert_use-robustness_enough_information',
        'likkert_use-robustness_scalability', 'robustness_challenge', 'robustness_advantage'
    ]

    if n_clicks == 0:
        print('not_relevant')
        return (
            *[stored_data.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            *[dash.no_update] * (len(input_ids) + 2),
            False,
            dash.no_update,
            *[dash.no_update] * len(PAGES),
            dash.no_update,
            False
        )

    print('robustness activated')
    values = [
        coding, crop_loss, robustness, tradeoff, general_interactions, interaction_least_productivity_loss,
        easy, confidence, enough_information, scalability, robustness_challenge, robustness_advantage
    ]

    validation_styles, stored_data, final_comment, final_style = validate_and_store_data(
        input_ids, values, stored_data)
    if final_style['color'] == '#5cb85c':
        stored_data['completed_pathways_robustness'] = 'yes'
        current_step = get_step_from_pathname(stored_data['current_url'])
        new_step = min(current_step + 1, len(PAGES) - 1)
        to_store_complete = True

        new_url = PAGES[new_step]['url']
        stored_data['current_url'] = new_url

        # Select the correct layout based on the new step
        content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(new_step)

        return (
            *[stored_data.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            content, *page_names, stored_data['current_url'], False)
    else:
        stored_data['completed_pathways_robustness'] = 'no'
        to_store_complete = False
        return (
            *[stored_data.get(in_id, []) if in_id in ['robustness', 'tradeoff', 'interaction_least_productivity_loss'] else stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, True)

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
        Output('storage-general', 'data', allow_duplicate=True),
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
        Output('to_store-complete', 'data', allow_duplicate=True),
        Output('page-content', 'children', allow_duplicate=True),
        *[Output(f"step-{i}-link", "children", allow_duplicate=True) for i in range(len(PAGES))],
        Output('url', 'pathname', allow_duplicate=True),
        Output("progress_modal", "is_open", allow_duplicate=True),
        Output('end_modal', 'is_open', allow_duplicate=True)
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
        State('storage-general', 'data'),
        State('url', 'pathname')
    ],
    prevent_initial_call=True
)
def handle_pathways_maps(n_clicks, first_measure, number_measures, most_flexible1_5, most_flexible4,
                         timing_shifts, ditch_shift, easy, confidence, enough_information, scalability,
                         pathways_challenge, pathways_advantage, stored_data, url):
    print('pathways called')
    input_ids = [
        'first_measure', 'number_measures', 'most_flexible15', 'most_flexible4', 'timing_shifts', 'ditch_shift',
        'likkert_use-pathways_maps_easy', 'likkert_use-pathways_maps_confidence',
        'likkert_use-pathways_maps_enough_information', 'likkert_use-pathways_maps_scalability', 'pathways_challenge',
        'pathways_advantage'
    ]

    if n_clicks == 0:
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            *[dash.no_update] * (len(input_ids) + 2),
            False,
            dash.no_update,
            *[dash.no_update] * len(PAGES),
            dash.no_update,
            False,
            False
        )

    print('pathways activated')
    values = [
        first_measure, number_measures, most_flexible1_5, most_flexible4, timing_shifts, ditch_shift,
        easy, confidence, enough_information, scalability, pathways_challenge, pathways_advantage
    ]

    validation_styles, stored_data, final_comment, final_style = validate_and_store_data(
        input_ids, values, stored_data)
    if final_style['color'] == '#5cb85c':
        stored_data['completed_pathways_maps'] = 'yes'
        current_step = get_step_from_pathname(stored_data['current_url'])
        new_step = min(current_step + 1, len(PAGES) - 1)
        to_store_complete = True

        new_url = PAGES[new_step]['url']
        stored_data['current_url'] = new_url

        # Select the correct layout based on the new step
        content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(new_step)

        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, False, True)

    else:
        stored_data['completed_pathways_maps'] = 'no'
        to_store_complete = False
        return (
            *[stored_data.get(in_id, None) for in_id in input_ids],
            stored_data,
            final_comment, final_style,
            *validation_styles, to_store_complete,
            dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, True, False)