from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, INTERACTION_VIZ, SYSTEM_ANALYSIS_FOCUS
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL

from dashapp import dash

dash.register_page(__name__, path='/4-system_analysis')

introduction_text = [
    "Until now, we only considered the perspective from on actor and risk to find pathways that work best across uncertainties and interactions."
    "However, other actors might do the same, so the question arises which combination of the shortlisted individual pathways go best together."
    "This is what can be explored here. You can explore how a specific combination of pathways perform across all relevant objectives and what this means"
    "with regards to the timing of decision points."
]

selection_options = html.Div([
    html.Div([
            html.Label('b) Looking at ...', className='mb-1'),
            dbc.Select(
                id='system_analysis_focus',
                options=[{'label': key, 'value': value} for key, value in SYSTEM_ANALYSIS_FOCUS.items()],
                className="mb-3"
            ),
        ], style={'marginBottom': '20px'}),
    html.Div(id='other_selection_options')
])


fig_explanation = [html.Div([html.P('Please select what you want to look at')], id='system_analysis_focus_figure')
   ]

testing_viz_questions = html.Div([
    html.P([html.I(INTRO_TEXT)]),
single_output_question(
        'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0, how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
        'system_analysis_pathways_1560-input',
        'number'
    ),
single_output_question(
        'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0, how many measures  are implemented for Farmer - Flood Pathway 1 in a 4 \u2103 climate scenario?',
        'system_analysis_pathways_1530-input',
        'number'
    ),
single_choice(
            'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',
            'system_analysis_pathways_which_better-input',
    {'Municipality - Flood Pathway 3': 3,
'Municipality - Flood Pathway 6': 6
     },
            'Dropdown'),
single_output_question(
        'Looking at Pathways Performance with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 6 and Shipping - Drought Pathway 0, what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
        'system_analysis_performance_1560-input',
        'number'
    ),
single_output_question(
        'Looking at Pathways Maps with the pathway combination Farmer Flood - Pathway 1, Farmer - Drought Pathway 5, Municipality - Flood Pathway 3 and Shipping - Drought Pathway 0, what are the expected Farmer - Flood Costs in a 4 \u2103 climate scenario?',
        'system_analysis_performance_1530-input',
        'number'
    ),
single_choice(
            'Which of the two considered Municipality Flood Pathways is more attractive from a Farmer - Flood perspective in a 4 \u2103 climate scenario?',
            'system_analysis_performance_which_better-input',
    {'Municipality - Flood Pathway 3': 3,
'Municipality - Flood Pathway 6': 6
     },
            'Dropdown'),
])


survey_questions = html.Div([
likkert_scale(
    'I find the Pathways Maps Figure easy to understand',
    'likkert_use-system_analysis_pathways_easy',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
likkert_scale(
    'I find the Performance Robustness Figure easy to understand',
    'likkert_use-system_analysis_performance_easy',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),

    likkert_scale(
    'I am confident that I read the Pathways Maps Figure correctly to inform the decision-choice',
    'likkert_use-system_analysis_pathways_confidence',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
likkert_scale(
    'I am confident that I read the Performance Robustness Figure correctly to inform the decision-choice',
    'likkert_use-system_analysis_performance_confidence',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    likkert_scale(
        'The Pathways Maps Figure provides enough information to justify your answer',
        'likkert_use-system_analysis_pathways_enough_information',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
        ),
likkert_scale(
        'The Performance Robustness Figure provides enough information to justify your answer',
        'likkert_use-system_analysis_performance_enough_information',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
        ),
likkert_scale(
        'I would use the Pathways Maps Figure for similar problems',
        'likkert_use-system_analysis_pathways_scalability',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    likkert_scale(
        'I would use the Performance Robustness Figure for similar problems',
        'likkert_use-system_analysis_performance_scalability',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    long_text(
        'Please briefly describe one or two challenges you had when reading the figures (if any)',
        'system_analysis_challenge'),

    long_text(
        'Please briefly describe one or two things you find useful about this figures (if any)',
        'system_analysis_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers(
        {'type': 'submit-survey', 'index': 5},
        'system_analysis-validation'),
    ]
)

text_field = create_instructions(introduction_text, selection_options, fig_explanation, testing_viz_questions, survey_questions)


visualization = dbc.Col(
    [

        dbc.Row(
            dcc.Loading(
            id="loading-spinner",
            type="circle",  # or "dot" or "default"
            children=[html.Div(id='system_analysis-graph')], style={
                'alignItems': 'top',
                'height': '100%',  # Ensure Row fills the Col height
                'display': 'flex',  # Flex display for row layout
                'flex-grow': '1'  # Allow row to grow and fill space
            }
        ),
            # id='system_analysis-graph',

        ),

    ],
    style=VIZ_STYLE_FIG,
    width=12-TEXTFIELD_WIDTH
)

layout_E = dbc.Row(
    [
        dbc.Col(
            [
                text_field
            ],
            width=TEXTFIELD_WIDTH,
        ),
        visualization,

        PROGRESS_MODAL,
        FINAL_MODAL
    ],
    style={'height': LAYOUT_HEIGHT}
)



