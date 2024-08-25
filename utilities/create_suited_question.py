import dash_bootstrap_components as dbc
from dash import dcc, html
from utilities.create_highlighted_word import create_highlighted_word
from components.explanations import *


def single_output_question(question, question_id, type='number'):
    """
    Create a single number input question.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the input element.
    type (str): The type of input element (default is 'number').

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the number input question.
    """
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            dbc.FormText(id=f'{question_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            dbc.Input(id=question_id, type=type, className="mb-3"),
            # dbc.FormText("Please enter a number.", color="muted"),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
    ])

def multiple_choice(question, question_id, option_dict):
    """
    Create a multiple-choice question using checkboxes.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the checklist element.
    option_dict (dict): Dictionary of options with labels as keys and values.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the multiple-choice question.
    """
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            dbc.FormText(id=f'{question_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            dbc.Checklist(
                id=question_id,
                options=[{'label': key, 'value': element} for key, element in option_dict.items()],
                inline=True,
                value=[],
                className="mb-3"
            ),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
    ])

def single_choice(question, question_id, option_dict, type='Radio'):
    """
    Create a single-choice question using radio buttons.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the radio items element.
    option_dict (dict): Dictionary of options with labels as keys and values.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the single-choice question.
    """
    if type == 'Radio':
        type_question = dbc.RadioItems(
                id=question_id,
                options=[{'label': key, 'value': element} for key, element in option_dict.items()],
                inline=True,
                className="mb-3"
            )
    elif type == 'Dropdown':
        type_question = dbc.Select(
            id=question_id,
            options=[
                {'label': key, 'value': element} for key, element in option_dict.items()
            ]
        )
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            dbc.FormText(id=f'{question_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            type_question,
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
    ])

def gender_question(question):
    """
    Create a gender selection question using radio buttons.

    Parameters:
    question (str): The question text.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the gender question.
    """
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for="gender-radio", style={'fontWeight': 'bold'}),
            dbc.FormText(id='gender-radio-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            dbc.RadioItems(
                id='gender-radio',
                options=[
                    {'label': 'woman', 'value': 'woman'},
                    {'label': 'man', 'value': 'man'},
                    {'label': 'non-binary', 'value': 'non_binary'},
                    {'label': 'prefer not to say', 'value': 'Prefer not to say'},
                    {'label': 'prefer to self-describe', 'value': 'Prefer to self-describe'},
                    {'label': 'other', 'value': 'Other'}
                ],
                inline=False,
                className="mb-3"
            ),
            dcc.Input(
                id='self-describe-input',
                type='text',
                placeholder='Please describe...',
                style={'display': 'none'}  # Initially hidden
            ),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
            # dbc.FormText("Please select your gender.", color="muted"),
        ])
    ])

def visual_impairments():
    """
    Create a question about visual impairments using radio buttons.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the visual impairments question.
    """
    question = "Do you have any visual impairments or conditions that might influence the way you perceive visual content?"
    return dbc.Row([
        dbc.Col([
            dbc.Label(
                [question], html_for="impairment-radio", style={'fontWeight': 'bold'}),
            dbc.FormText(id='impairment-radio-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            dbc.RadioItems(
                id='impairment-radio',
                options=[
                    {'label': 'No', 'value': 'No'},
                    {'label': 'Yes', 'value': 'Yes'},
                    {'label': "I don't know", 'value': 'IdontKnow'},
                ],
                inline=False,
                className="mb-3"
            ),
            dcc.Input(
                id='self-describe-input_visual',
                type='text',
                placeholder='Please describe...',
                style={'display': 'none'}  # Initially hidden
            ),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),

            # dbc.FormText("Please select one option.", color="muted"),
        ])
    ])


def likkert_scale(question, question_id, input_list):
    """
    Create a Likert scale question using a slider.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the slider element.
    input_list (list): List of labels for the Likert scale.
    comment (str): Comment or instruction for the question.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the Likert scale question.
    """
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            dbc.FormText(id=f'{question_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            html.Div(
                dcc.Slider(
                    id=question_id,
                    min=1,
                    max=5,
                    step=1,
                    marks={i: label for i, label in enumerate(input_list, start=1)},
                    value=None,
                    className="custom-slider"
                ),
                className="slider-container",
                style={'width': '90%', 'marginLeft': '0px', 'marginRight': '0px'}
            ),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
    ], style={'marginBottom':'2vh'})




def multi_likkert_scale_with_explanation(question, question_id, input_list, multi_comments):
    """
    Create multiple Likert scale questions using sliders.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the sliders.
    input_list (list): List of labels for the Likert scale.
    multi_comments (list): List of comments or instructions for each slider.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing multiple Likert scale questions.
    """
    sliders = []
    for comment in multi_comments:
        adjusted_comment = comment.replace(" ", "_")
        relevant_modal = matching_dict.get(adjusted_comment + '_explanation',None)
        slider_id = f'{question_id}_{adjusted_comment}'
        slider = html.Div([
            html.Div([html.I(comment), html.Small('   '), html.Small(
            create_highlighted_word('(?)', adjusted_comment + '_explanation'),
            className="text-muted ml-2",
            style={'display': 'inline'}
        )]),
            dbc.FormText(id=f'{slider_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            relevant_modal,
            html.Div(
                dcc.Slider(
                id=slider_id,
                min=1,
                max=5,
                step=1,
                marks={i: label for i, label in enumerate(input_list, start=1)},
                value=None,
                # included=False,
                className="custom-slider",
            ),
                className="slider-container",
                style={'width': '90%', 'marginLeft': '0px', 'marginRight': '0px'}
            ),
            html.Br(),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
        sliders.append(slider)

    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            html.Div(sliders),
        ])
    ])


def multi_likkert_scale(question, question_id, input_list, multi_comments):
    """
    Create multiple Likert scale questions using sliders.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the sliders.
    input_list (list): List of labels for the Likert scale.
    multi_comments (list): List of comments or instructions for each slider.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing multiple Likert scale questions.
    """
    evaluation_ids = ['easy', 'confidence', 'enough_information', 'scalability']
    sliders = []
    for i, comment in enumerate(multi_comments):
        if question_id.startswith('likkert_use'):
            adjusted_comment = evaluation_ids[i]
        else:
            adjusted_comment = comment.replace(" ", "_")
        slider_id = f'{question_id}_{adjusted_comment}'
        slider = html.Div([
            html.Div([html.I(comment)]),
            dbc.FormText(id=f'{slider_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            html.Div(
                dcc.Slider(
                    id=slider_id,
                    min=1,
                    max=5,
                    step=1,
                    marks={i: label for i, label in enumerate(input_list, start=1)},
                    value=None,
                    # included=False,
                    className="custom-slider"
                ),
                className="slider-container",
                style={'width': '90%', 'marginLeft': '0px', 'marginRight': '0px'}
            ),
            html.Br(),
            html.Hr(style={'borderWidth': "1px", 'borderColor': 'grey'}),
        ])
        sliders.append(slider)

    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            html.Div(sliders),
        ])
    ])


def long_text(question, question_id):
    """
    Create a long text input question using a textarea.

    Parameters:
    question (str): The question text.
    question_id (str): The unique identifier for the textarea element.

    Returns:
    dbc.Row: A Dash Bootstrap Components Row containing the long text input question.
    """
    return dbc.Row([
        dbc.Col([
            dbc.Label([question], html_for=question_id, style={'fontWeight': 'bold'}),
            dbc.FormText(id=f'{question_id}-validation', color='danger', children='This field is required.',
                         style={'display': 'none'}),
            dbc.Textarea(
                id=question_id,
                placeholder='Enter your multi-line comment here...',
                style={'width': '100%', 'height': '10vh'},
                className="mb-3"
            ),
        ])
    ])

