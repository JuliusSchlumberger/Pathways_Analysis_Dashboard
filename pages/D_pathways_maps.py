from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT, MEASURE_ALTERNATIVES, INTERACTIONS
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL
from dashapp import dash

dash.register_page(__name__, path='/3-pathways-maps')

introduction_text = [
    "We need to consider ",
    create_highlighted_word(
        'pathways maps ',
        'Pathways_Map_explanation'
    ),
    "alongside performance robustness because they visualize the sequence, timing of decisions and transfers. This helps us "
    "understand when and how to switch between measures as conditions change. While robustness focuses on ensuring a "
    "strategy works across different scenarios, pathways maps help us plan the best route forward by identifying "
    "critical ",
    create_highlighted_word(
        'timings or conditions for action.',
        'timing_explanation'),
    html.P(
        " and the path-dependency. Pathways maps can look different depending on which scenario is considered, or depending on which "
        "interactions are considered."
    ),
    Pathways_Map_explanation,
    timing_explanation
]

selection_options = html.Div([
    html.Div([
        html.Label('a) Climate Scenario', className='mb-1'),
        dbc.Select(
            id='scenarios-maps',
            options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],
        )], style={'marginBottom': '20px'}),
    html.Div([
            html.Label('b) Accounting for interactions with...', className='mb-1'),
            dbc.Select(
                id='multi_sectoral_interactions_maps',
                options=[{'label': key, 'value': value} for option in INTERACTIONS['flood_agr'] for key, value
                         in
                         option.items()],
                value='no_interactions',
                className="mb-3"
            ),
        ], style={'marginBottom': '20px'}),
])


fig_explanation = [html.P("This figures represents a 'Metro-map' through time (starting at the left, moving to the right). "
                          "The points where lines split or intersect indicate key moments where a decision is needed to "
                          "either stay on the current path or switch to a new one. This ensures that the chosen "
                          "pathway remains effective as circumstances evolve."),
                   html.P("The map shows how we can get to a certain point in time and what future measures we could "
                          "implement."),
                   html.P('You can hover over the markers to learn about the type of decision-point below the figure '
                          'and click on it to see what future options you have from this point onwards.')
                         ]

testing_viz_questions = html.Div([
    html.P([html.I(INTRO_TEXT)]),

    single_output_question(
        'In which year is the first measure needed in a 1.5 \u2103 climate scenario with no pathway interactions considered?',
        'first_measure-input',
        'number'
    ),

    single_output_question(
        'What is the maximum number of measures that need to be implemented in one pathway in a '
        '1.5 \u2103 climate scenario over the 100 years with no pathway interactions considered?',
        'number_measures-input',
        'number'
    ),

    # multiple_choice(
    #     'In a 1.5 \u2103 climate scenario, which pathway(s) seem to be the most flexible?',
    #     'most_flexible15-input',
    #     OPTION_DICT
    # ),

    single_choice(
            'In a 1.5 \u2103 climate scenario, which first implemented measure offers the most flexibility with regards to future options?',
            'most_flexible15-input',
            MEASURE_ALTERNATIVES,
            'Dropdown'),
single_choice(
            'In a 4 \u2103 climate scenario, which first implemented measure offers the most flexibility with regards to future options?',
            'most_flexible4-input',
            MEASURE_ALTERNATIVES,
            'Dropdown'),
    # multiple_choice(
    #     'Which pathway(s) seem to be the most flexible alternatives in a 4 \u2103 climate scenario?',
    #     'most_flexible4-input',
    #     OPTION_DICT
    # ),

    single_choice(
        'When accounting for the presence of Farmer - Drought interactions, what is the general effect on the timing of measure implementation compared to the case without interactions '
        'in a 4 \u2103 climate scenario?',
        'timing_shifts-input',
        {
            'measures are implemented mostly earlier': 'earlier',
            'measures are implemented mostly later': 'later',
            'there are no interaction effects': 'no_effect',
            'it is not clear': 'notclear'
        },
        'Dropdown'
    ),
    single_output_question(
        'When accounting for the presence of Farmer - Drought interactions, by how many years does the '
        'implementation of "Large Dike elevation increase" in pathway 6 shift in a 4 \u2103 climate scenario compared to the case without interactions (use negative values if implementation takes place earlier, otherwise positive values)?',
        'ditch_shift-input',
        'number'
    ),
])


survey_questions = html.Div([
likkert_scale(
    'I find this figure easy to understand',
    'likkert_use-pathways_maps_easy',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),

    likkert_scale(
    'I am confident that I read this figure correctly to inform the decision-choice',
    'likkert_use-pathways_maps_confidence',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    likkert_scale(
        'This visualization provides enough information to justify your answer',
        'likkert_use-pathways_maps_enough_information',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
        ),
    likkert_scale(
        'I would use this visualisation for similar problems',
        'likkert_use-pathways_maps_scalability',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    long_text(
        'Please briefly describe one or two challenges you had when reading the figure (if any)',
        'pathways_challenge'),

    long_text(
        'Please briefly describe one or two things you find useful about this figure (if any)',
        'pathways_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers(
        {'type': 'submit-survey', 'index': 4},
        'pathways_maps-validation'),
    ]
)

text_field = create_instructions(introduction_text, selection_options, fig_explanation, testing_viz_questions, survey_questions)


visualization = dbc.Col(
    [

        dbc.Row(
            id='pathways-graph', style={
                'alignItems': 'top',
                'height': '100%',  # Ensure Row fills the Col height
                'display': 'flex',  # Flex display for row layout
                'flex-grow': '1'  # Allow row to grow and fill space
            }

        ),

    ],
    style=VIZ_STYLE_FIG,
    width=12-TEXTFIELD_WIDTH
)

layout_D = dbc.Row(
    [
        dbc.Col(
            [
                text_field
            ],
            width=TEXTFIELD_WIDTH,
        ),
        visualization,
        PROGRESS_MODAL,
        FINAL_MODAL,

    ],
    style={'height': LAYOUT_HEIGHT}
)


