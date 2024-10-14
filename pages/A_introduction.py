import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from utilities.create_highlighted_word import create_highlighted_word
from components.explanations import *
from assets.static_inputs import INTRO_TEXT
from utilities.create_suited_question import *
from utilities.submission_button import submit_answers
from utilities.instruction_template import create_instructions
from components.progress_modal import PROGRESS_MODAL, FINAL_MODAL
import plotly.io as pio
import base64
from PIL import Image
from io import BytesIO
import json

dash.register_page(__name__, path='/0-introduction')

figure_identifier = 'assets/figures/Waasmodel_with_legend.json'

with open(figure_identifier, 'r') as f:
    data = json.load(f)

# Decode the Base64 string
img_data = base64.b64decode(data['image'])

# Convert the binary data back into an image
image = Image.open(BytesIO(img_data))


# Convert the image to a Base64 string to embed in HTML
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")


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
                "To test this dashboard, you will take on the role as a farmer interested in managing flood risk. You will be asked to answer questions "
                "based on visualizations presented."),
            pathways_explanation,
        ]),
    html.P("This Dashboard will guide you through the following analysis steps:"),
    html.Ol([

            html.Li([
                html.B('Measure Sequences: '),
                'You will learn about the measures you can take as a farmer and which sequences of these measures were considered as possible pathway alternatives.'
            ]),
            html.Li([
                html.B('Pathways Performance Robustness: '),
                'You will learn how these pathway alternatives perform under uncertainty.'
            ]),
            html.Li([
                html.B('Pathways Maps: '),
                'You will learn how different pathways map out in time.'
            ]),
            html.Li([
                html.B('System Analysis: '),
                'While you focused on your own interests as a farmer in the first three steps to identify pathways that work best for you, you will broaden this focus in the last step considering multiple actors and their objectives.'
            ]),
        ])
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
            ['never', 'rarely', 'sometimes', 'often', 'every\u00A0day']
        ),

        multi_likkert_scale_with_explanation(
            "What is your experience with the following visualization techniques?",
            "viztype-input",
            ['never', 'rarely', 'sometimes', 'often', 'every\u00A0day'],
            ["Stacked Bar Chart", "Parallel Coordinates Plot", "Heatmap", "Pathways Map"]
        ),
        *submit_answers(
            {'type': 'submit-survey', 'index': 1},
            'introduction-validation'
        ),
    ],
)

step0_instruction = create_instructions(
    introduction_text,
    False,
    False,
    False,
    survey_questions
)


visualization = dbc.Col(
    [
        # dbc.Row(
        #     dcc.Graph(id='introduction-image', figure=fig, responsive=False, config={'displayModeBar': False})
        # )
        dbc.Row(
            html.Img(id='introduction-image', src=f"data:image/png;base64,{img_str}", style={'max-width': '100%',
                'height': '80vh',
                'margin': 'auto'}),
            style={
                'height': '80vh',
                'display': 'flex',
                # 'justifyContent': 'center',
                # 'alignItems': 'top',
                'margin': '0px',
                # 'padding': '5%',
            }
        ),
    ],
    style={
        'height': '78vh',  # Set the height of the column
        'display': 'flex',  # Use Flexbox for alignment
        'justifyContent': 'center',  # Center horizontally
        'alignItems': 'top',  # Center vertically
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
        visualization,
        PROGRESS_MODAL,
        FINAL_MODAL,

    ],
)



