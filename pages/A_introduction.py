import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from utilities.create_highlighted_word import create_highlighted_word
from components.explanations import *
from assets.static_inputs import INTRO_TEXT
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions

dash.register_page(__name__, path='/0-introduction')


introduction_text = [
    html.P(
        [
            "Imagine the following case: a farmers union, shipping company and a mayor each want to identify ",
            create_highlighted_word("pathways ", "pathways_explanation"),
            "to adapt to increasing risk of floods and droughts due to climate change in the Netherlands over the "
            "coming 100 years. To support each of their analysis of viable options, we developed a dashboard that "
            "guides them through the analysis step by step.",
            html.Br(),
            html.Br(),
            html.B(
                "To test this dashboard, you will take on the role as a farmer. You will be asked to answer questions "
                "based on visualizations presented."),
            pathways_explanation,
        ]
    )
]

step0_fig_explanation = [
    html.P(
        'This figure shows the synthetic case study area: a river stretch used for shipping with dike embankments, some '
        'cities and a lot of agricultural land.'
    )
]

survey_questions = html.Div(
    [
        html.P(
            html.I(INTRO_TEXT)
        ),
        visual_impairments(),
        multiple_choice(
            "What is your field of work?",
            'work-input',
            {
                "Research": "research",
                'Public Administration': 'public_administration',
                'Private sector': 'private_sector',
                'Other': 'other'
            }
        ),

        single_output_question(
            "What are your areas of expertise (use key terms and separate by ';')",
            'expertise-input',
            'text'
        ),

        likkert_scale(
            "How often do you use visualizations for analysis?",
            'use_frequency-input',
            ['never', 'rarely', 'sometimes', 'often', 'every day']
        ),

        multi_likkert_scale_with_explanation(
            "What is your experience with the following visualization techniques?",
            "viztype-input",
            ['never', 'rarely', 'sometimes', 'often', 'every day'],
            ["Stacked Bar Chart", "Parallel Coordinates Plot", "Heatmap", "Pathways Map"]
        ),
        *submit_answers(
            'submit-survey-introduction',
            'introduction-validation'
        ),
    ],
)

step0_instruction = create_instructions(
    introduction_text,
    False,
    False,
    survey_questions
)


visualization = dbc.Col(
    [
        dbc.Row(
            html.Img(id='introduction-image', src='assets/figures/Waasmodel.png'),
            style={
                'width': '70%',
                'justifyContent': 'center',
                'alignItems': 'center',
                'display': 'flex',
                'padding': '5%',
            }
        ),
    ],
    style={
        'height': '78vh',  # Set the height of the column
        'display': 'flex',  # Use Flexbox for alignment
        'justifyContent': 'center',  # Center horizontally
        'alignItems': 'center',  # Center vertically
    },
    width=6
)


layout_A = dbc.Row(
    [
        dbc.Col(
            [
                step0_instruction
            ],
            width=6,
        ),
        visualization
    ],
)



