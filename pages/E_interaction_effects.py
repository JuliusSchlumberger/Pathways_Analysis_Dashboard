from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT, INTERACTION_VIZ
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from dashapp import dash

dash.register_page(__name__, path='/4-interaction-effects')


step4_intro = [
         "So far we only considered the robustness & timings of pathways in case the measures could be implemented independently. "
         "However, in reality the system will change due to measures implemented for other sectors or other risks. "
         "Here we can explore how these ",
    create_highlighted_word('interactions ', 'interactions_explanation'), " influence the robustness and timing of the pathways. ",
        interaction_explanation
    ]

step4_fig_explanation = html.Div(id='interaction-figure-paragraph', style={'marginTop': '20px'})

step4_selections = html.Div([
    html.Div([
            html.Label('a) Accounting for interactions with... (multiple-choice)', className='mb-1'),
            dbc.Checklist(
                id='multi_sectoral_interactions',
                options=[],
                inline=True,
                className="mb-3"
            ),
        ], style={'marginBottom': '20px'}),
    html.Div([
            html.Label('b) Explore interaction effects on...', className='mb-1'),
        dcc.Dropdown(id='interaction_plot_options',
                     options=[{'label': option, 'value': INTERACTION_VIZ[option]} for option in INTERACTION_VIZ],
                     )
        ], style={'marginBottom': '20px'})
    ])

survey_question = html.Div([
    html.P([html.I(INTRO_TEXT)]),



multi_likkert_scale("Likkert-Evaluation questions",
                        'likkert_use-interaction_effects',
                        ['I totally disagree', '', '', '', 'I totally agree'],
                        ['I find this figure easy to understand',
                         'I am confident that I read this figure correctly to inform the decision-choice',
                         'This visualization provides enough information to justify a potential choice?',
                         'I would use this visualisation for similar problems'
                         ]),

    long_text('Please briefly describe one or two challenges you had when reading the figure (if any)',
              'interaction_effects_challenge'),

    long_text('Please briefly describe one or two things about this figure you find useful (if any)',
              'interaction_effects_advantage'),

    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-interaction_effects', 'interaction_effects-validation'),

    ])


step4_instruction = create_instructions(step4_intro, step4_selections, step4_fig_explanation, survey_question)

visualization = dbc.Col([
    dbc.Row(id='interactions-graph', style={'alignItems': 'top'}),
], style=VIZ_STYLE_FIG, width=12-TEXTFIELD_WIDTH)


layout_E = dbc.Row(
    [dbc.Col([
        # tabs,
        step4_instruction], width=TEXTFIELD_WIDTH),
     visualization],
    style={'height': LAYOUT_HEIGHT}
)
