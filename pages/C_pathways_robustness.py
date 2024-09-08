from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT, INTERACTIONS
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL
from dashapp import dash
import random

random_default = random.choice(list(WHICH_OPTIONS.keys()))

dash.register_page(__name__, path='/2-pathways-robustness')

introduction_text = [
    "Now, let's explore the performance ",
    create_highlighted_word('robustness', "robustness_explanation"),
    " of the considered flood risk ",
    create_highlighted_word("pathways", "pathways_explanation"),
    " for the farmer. Robustness is measured across multiple objectives. ",
    " You can explore the robustness",
    " of the pathways over different different time horizons and under different ",
    create_highlighted_word("climate scenarios", 'scenario_explanation'),
    ". Additionally, other actors are also implementing pathways which might have ",
    create_highlighted_word('interaction effects ', 'interaction_explanation'),
    " that could influence the performance robustness of the pathways.",
    interaction_explanation,
    pathways_explanation,
    robustness_explanation,
    scenario_explanation
    ]

selection_options = html.Div([
            html.Div([
                html.Label('a) Timehorizon for Evaluation', className='mb-1'),
                dbc.Select(
                    id='timehorizon',
                    options=[{'label': option, 'value': TIMEHORIZONS[option]} for option in TIMEHORIZONS],
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label('b) Climate Scenario', className='mb-1'),
                dbc.Select(
                        id='scenarios',
                        options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],

                    )], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('c) Robustness quantification (default - no choice necessary)', className='mb-1'),
                dbc.Select(
                        id='robustness_metric',
                    options=[{'label': option, 'value': ROBUSTNESS_METRICS[option]} for option in ROBUSTNESS_METRICS],
                        # options=[{'label': option, 'value': ROBUSTNESS_METRICS[option], 'disabled': True if option != "mean across scenarios" else False
                        #     } for option in ROBUSTNESS_METRICS],
                        # value=list(ROBUSTNESS_METRICS.values())[0],
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label('Figure type', className='mb-1'),
                dbc.Select(
                    id='options',
                    # # Comment out the rest
                    options=[
                        {
                            'label': random_default,
                            'value': WHICH_OPTIONS[random_default],
                        }
                    ],
                    # value=random_default,  # Set the randomized value as the default
                ),
            ], style={'marginBottom': '20px'}),
    html.Div([
            html.Label('d) Accounting for interactions with...', className='mb-1'),
            dbc.Select(
                id='multi_sectoral_interactions_robustness',
                options=[{'label': key, 'value': value} for option in INTERACTIONS['flood_agr'] for key, value
                            in
                            option.items()],
                value= 'no_interactions',
                # inline=True,
                className="mb-3"
            ),
        ], style={'marginBottom': '20px'}),
])

fig_explanation = html.Div("This need to be updated",
                                 id='dynamic-figure-paragraph',
                                 )

testing_viz_questions = html.Div([
    html.P([html.I(INTRO_TEXT)]),
    single_output_question(
        'What do the colors represent in the figure?',
        'coding-input',
        'text'),

    single_output_question('How much Crop Productivity Loss [%] do we expect for Pathway 5 over a time horizon of 60 years in the 4 \u2103 climate scenario  with no pathway interactions considered?',
                           'crop_loss-input', 'number'),

    multiple_choice('In the 4 \u2103 climate change scenario, which pathway(s) is most robust at the time horizon of 60 years  with no pathway interactions considered?',
                    'robustness-input', OPTION_DICT),

    multiple_choice(
        'Which pathway(s) results in the highest Impacted Lifestock '
        'after 100 years in a 1.5 \u2103 climate scenario with no pathway interactions considered?',
        'tradeoff-input',
        OPTION_DICT),
    single_choice(
        'When accounting for the presence of Farmer - Drought interactions, do we experience more synergy or more trade-off effects in a 1.5 \u2103 climate scenario over the next 60 years?',
        'general_interactions-input',
        {
            'more synergy effects': 'synergies',
            'more trade-off effects': 'tradeoffs',
            'there are no interaction effects': 'no_effect',
            'it is not clear': 'notclear'
        },
        'Dropdown'
    ),
    multiple_choice(
        'When accounting for the presence of Farmer - Drought strategies, which pathway(s) show the best '
        'robustness regarding Crop Productivity Loss in a 4 \u2103 climate scenario over the next 60 years?',
        'interaction_least_productivity_loss-input',
        OPTION_DICT
    ),
])


survey_questions = html.Div([
likkert_scale(
    'I find this figure easy to understand',
    'likkert_use-robustness_easy',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),

    likkert_scale(
    'I am confident that I read this figure correctly to inform the decision-choice',
    'likkert_use-robustness_confidence',
    ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    likkert_scale(
        'This visualization provides enough information to justify your answer',
        'likkert_use-robustness_enough_information',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
        ),
    likkert_scale(
        'I would use this visualisation for similar problems',
        'likkert_use-robustness_scalability',
        ['totally disagree', '', '', '', 'totally\u00A0agree'],
    ),
    long_text(
        'Please briefly describe one or two challenges you had when reading the figure (if any)',
        'robustness_challenge'),

    long_text(
        'Please briefly describe one or two things you find useful about this figure (if any)',
        'robustness_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers(
        {'type': 'submit-survey', 'index': 3},
        'pathways_robustness-validation')
    ]
)


text_field = create_instructions(introduction_text, selection_options, fig_explanation, testing_viz_questions, survey_questions)


visualization = dbc.Col([
    dbc.Row(id='robustness-graph', style={'alignItems': 'top',
                                          'height': '100%',  # Ensure Row fills the Col height
                                          'display': 'flex',  # Flex display for row layout
                                          'flex-grow': '1'  # Allow row to grow and fill space
                                          }),
], style=VIZ_STYLE_FIG, width=12-TEXTFIELD_WIDTH)


layout_C = dbc.Row(
    [dbc.Col([
    text_field
    ], width=TEXTFIELD_WIDTH),
     visualization,
    PROGRESS_MODAL,
    FINAL_MODAL],
    style={'height': LAYOUT_HEIGHT}
)
