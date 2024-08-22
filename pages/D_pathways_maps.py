from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from dashapp import dash

dash.register_page(__name__, path='/3-pathways-maps')

introduction_text = [
    "We need to consider ",
    create_highlighted_word(
        'pathways maps ',
        'Pathways_Map_explanation'
    ),
    "alongside performance robustness because they visually show the sequence and "
    "timing of decisions. This helps us understand when and how to switch strategies as conditions change. "
    "While robustness focuses on ensuring a strategy works across different scenarios, pathways maps help us "
    "plan the best route forward by identifying critical ",
    create_highlighted_word(
        'timings for action.',
        'timing_explanation'),
    html.P(
        "Pathways maps can look differently depending on which scenario is considered, or depending on which "
        "interactions with other actors are considered"
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
                className="mb-3"
            ),
        ], style={'marginBottom': '20px'}),
])


fig_explanation = [html.P("This figures represents a 'Metro-map' through time (starting at the left, moving to right). "
                          "The points where lines split or intersect indicate key moments where a decision is needed to "
                          "either stay on the current path or switch to a new one, ensuring the chosen strategy remains "
                          "effective as circumstances evolve."),
                   html.P("It shows how we can get to a certain point in time and what future measures we could implement."),
                   html.P('You can hover over the markers to see how you get to a certain point to learn what needs to '
                          'happen at this decision point and what future options you have from this point onwards.')
                         ]

survey_questions = html.Div([
    html.P([html.I(INTRO_TEXT)]),

    single_output_question('In which year is the first measure needed in a 1.5 \u2103 climate scenario?',
                           'first_measure-input', 'number'),

single_output_question('What is the maximum number of measures that need to be implemented in a pathway in a 1.5 \u2103 climate scenario?',
                           'number_measures-input', 'number'),

    multiple_choice('In a 1.5 \u2103 climate scenario, which pathway(s) seem to be the most flexible alternatives?','most_flexible15-input', OPTION_DICT),
    multiple_choice('Which pathway(s) seem to be the most flexible alternatives in a 4 \u2103 climate scenario,?','most_flexible4-input', OPTION_DICT),
    single_choice('What is the general effect of the interactions on the timing of measure implementation when '
              'accounting for the presence of Farmer - Drought strategies in a 1.5 \u2103 climate scneario?',
              'timing_shifts-input',
              {'measures are implemented mostly earlier': 'earlier',
               'measures are implemented mostly later': 'later',
               'it is not clear': 'notclear'}),
    single_output_question('How many years did the implementation of "Ditch System" in pathway 1 shift for the presence of Farmer - Drought strategies in a 1.5 \u2103 climate scneario?',
                        'ditch_shift-input', 'number'),

    multi_likkert_scale("Likkert-Evaluation questions",
                        'likkert_use-pathways_maps',
                        ['I totally disagree', '', '', '', 'I totally agree'],
                        ['I find this figure easy to understand',
                         'I am confident that I read this figure correctly to inform the decision-choice',
                         'This visualization provides enough information to justify a potential choice?',
                         'I would use this visualisation for similar problems'
                         ]),

    long_text('Please briefly describe one or two challenges you had when reading the figure (if any)',
              'pathways_challenge'),

    long_text('Please briefly describe one or two things about this figure you find useful (if any)',
              'pathways_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-pathways_maps', 'pathways_maps-validation'),

])

text_field = create_instructions(introduction_text, selection_options, fig_explanation, survey_questions)


visualization = dbc.Col(
    [

        dbc.Row(
            id='pathways-graph',
            style={
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
    ],
    style={'height': LAYOUT_HEIGHT}
)


