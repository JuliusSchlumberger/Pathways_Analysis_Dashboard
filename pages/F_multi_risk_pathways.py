from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, INTERACTION_VIZ
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from dashapp import dash

dash.register_page(__name__)

step4_intro = [
         "So far we only considered the robustness & timings of pathways in case the measures could be implemented independently. "
         "However, in reality the system will change due to measures implemented for other sectors or other risks. "
         "Here we can explore how these ",
    create_highlighted_word('interactions ', 'interactions_explanation'), " influence the robustness and timing of the pathways. ",
        interaction_explanation
    ]

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

step4_fig_explanation = html.Div(id='interaction-figure-paragraph', style={'marginTop': '20px'})

survey_question = html.Div([
    html.P([html.I(INTRO_TEXT)]),
    single_output_question('How many years did the implementation of measure X in pathway 1 shift when accounting for the presence of farmer – drought pathways?',
                        'measure_shift-input', 'number'),

    single_output_question('How did the robustness of pathway X regarding Crop Losses change when accounting for presence of farmer – drought pathways?',
                        'robustness_change-input', 'text'),

    single_output_question('Name three flood-farmer pathways that experience strong trade-off effects from farmer – drought pathways',
                        'strong_tradeoffs-input', 'text'),

    single_output_question('Which pathway experiences the strongest synergistic effect from the general presence of farmer-drought pathways?',
                        'strong_synergy-input', 'text'),


    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-interaction_effects', 'interaction_effects-container'),
    dbc.Modal(
        [
            dbc.ModalHeader("Incomplete Form"),
            dbc.ModalBody(id="modal-body-interactions"),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),
        ],
        id="modal-interactions",
    )
    ])

step5_instruction = create_instructions(step4_intro, step4_selections, step4_fig_explanation, survey_question)

visualization = dbc.Col(
    [
        dbc.Row(id='pathways-graph', style={'alignItems': 'top', 'margin': '0', 'padding': '0'}),
    ],
    style={'height': '100vh', 'margin': '0', 'padding': '0'},
    width=8
)

layout_F = dbc.Row(
    [
        dbc.Col(
            [
                step5_instruction
            ],
            width=4,
            style={'height': '90vh', 'margin': '0', 'padding': '0'}
        ),
        visualization
    ],
    style={'height': '90vh', 'margin': '0', 'padding': '0'}
)


