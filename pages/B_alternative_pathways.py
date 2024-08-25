from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, ROH_DICT, MEASURE_ALTERNATIVES
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL
from dashapp import dash

dash.register_page(__name__, path='/1-measure-sequences')

introduction_text = [
    "Let's first explore what alternative measure sequences a farmer considers as part of ",
    create_highlighted_word("pathways", "pathways_explanation"),
    " to manage flood risk.",
    pathways_explanation,
    ]

selection_options = html.Div([
    html.Label('a) Actor and Risk (default - no choice necessary', className='mb-1'),
    dbc.Select(
        id='risk_owner_hazard',
        options=[
            # {'label': option, 'value': ROH_DICT[option], 'disabled': True if option != "Farmer - Flood" else False}
            # for option in ROH_DICT
            # {'label': option, 'value': ROH_DICT[option]}
            # for option in ROH_DICT
            {'label': list(ROH_DICT.keys())[0], 'value': list(ROH_DICT.values())[0]}
        ],
        value=list(ROH_DICT.values())[0],  # Optional: pre-select the fixed option
    ),
], style={'alignItems': 'start'})



fig_explanation = [html.P('This figure shows all considered measure sequences. It has the shape of a decision tree, '
                         'where sequences are built from left (1st measure) to the right (4th measure).'),
                         html.P('Hover over the items for additional information about the measures.')]


testing_viz_questions = html.Div(
    [
        html.P([html.I(INTRO_TEXT)]),
        single_output_question(
            'How many pathway alternatives do you have?',
            'pathway_number-input',
            'number'),

        single_output_question(
            'How many alternative pathways start with measure "flood resilient crops"?',
            'f_resilient_crops-input',
            'number'),

        # single_output_question(
        #     'Which measure is considered most often as the long-term measure (being implemented at a later stage)?',
        #     'long_term-input',
        #     'text'),
        single_choice(
                'Which measure is considered most often as the long-term measure (being implemented at a later stage)?',
                'long_term-input',
                MEASURE_ALTERNATIVES,
            'Dropdown',
        ),

        single_choice(
            'Which first implemented measure offers the most flexibility with regards to future options?',
            'flexibility-input',
            MEASURE_ALTERNATIVES,
            'Dropdown'
        ),
    ]
)

survey_questions = html.Div([
likkert_scale(
    'I find this figure easy to understand',
    'likkert_use-alternatives_easy',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),

    likkert_scale(
    'I am confident that I read this figure correctly to inform the decision-choice',
    'likkert_use-alternatives_confidence',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    likkert_scale(
        'This visualization provides enough information to justify your answer',
        'likkert_use-alternatives_enough_information',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
        ),
    likkert_scale(
        'I would use this visualisation for similar problems',
        'likkert_use-alternatives_scalability',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    #
    #
    #
    # multi_likkert_scale("Likkert-Evaluation questions",
    #                     'likkert_use-alternatives',
    #                     ['totally disagree', '', '', '', 'totally\u00A0agree'],
    #                     ['I find this figure easy to understand',
    #                     'I am confident that I read this figure correctly to inform the decision-choice',
    #                     'This visualization provides enough information to justify your answer',
    #                     'I would use this visualisation for similar problems'
    long_text(
        'Please briefly describe one or two challenges you had when reading the figure (if any)',
        'alternative_challenge'),

    long_text(
        'Please briefly describe one or two things you find useful about this figure (if any)',
        'alternative_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers(
        'submit-survey-alternative_pathways',
        'alternative_pathways-validation'),
]),




text_field = create_instructions(introduction_text, selection_options, fig_explanation, testing_viz_questions, survey_questions)


visualization = dbc.Col([
    dbc.Row(id='alternatives-graph', style={'alignItems': 'top'}),
], style=VIZ_STYLE_FIG, width=12-TEXTFIELD_WIDTH)


layout_B = dbc.Row(
    [dbc.Col([
        text_field], width=TEXTFIELD_WIDTH),
     visualization,
    PROGRESS_MODAL,
    FINAL_MODAL],
    style={'height': LAYOUT_HEIGHT}
)



