from dash import html

def create_instructions(intro_text, choices=False, figure_explanation=False, testing_viz_questions=False, questionaire=False):
    """
    Create an instructions template for a dashboard application.

    Parameters:
    intro_text (str): The introductory text for the instructions.
    choices (list or bool): A list of choice elements to be displayed or False if no choices.
    figure_explanation (list or bool): A list of figure explanation elements to be displayed or False if none.
    questionaire (list or bool): A list of questionnaire elements to be displayed or False if none.

    Returns:
    html.Div: A Dash HTML Div component containing the formatted instructions.
    """
    # Create choices section if choices are provided
    if choices:
        choices_instruction = [
            html.Hr(style={'borderWidth': "3px", 'borderColor': 'grey'}),
            html.H4("Specify the focus of the analysis"),
            html.Div(choices, style={'alignItems': 'start'}),
        ]
    else:
        choices_instruction = [html.Div('')]

    # Create figure explanation section if figure_explanation is provided
    if figure_explanation:
        figure_instruction = [
            html.Hr(style={'borderWidth': "3px", 'borderColor': 'grey'}),
            html.H4("How to read the figure on the right"),
            html.Div(figure_explanation, style={'marginTop': '20px'}),
        ]
    else:
        figure_instruction = [html.Div('')]

    # Create questionnaire section if questionaire is provided
    if testing_viz_questions:
        testing_viz_instruction = [
            html.Hr(style={'borderWidth': "3px", 'borderColor': 'grey'}),
            html.H4("Questions on the visualization"),
            html.Div(testing_viz_questions, style={'alignItems': 'start'}),
        ]
    else:
        testing_viz_instruction = [html.Div('')]

    if questionaire:
        questionaire_instruction = [
            html.Hr(style={'borderWidth': "3px", 'borderColor': 'grey'}),
            html.H4("Survey questions"),
            html.Div(questionaire, style={'alignItems': 'start'}),
        ]
    else:
        questionaire_instruction = [html.Div('')]

    # Combine all sections into the instruction div
    instruction = html.Div([
        html.Div(intro_text, style={'marginBottom': '1%'}),
        *choices_instruction,
        *figure_instruction,
        *testing_viz_instruction,
        *questionaire_instruction,
    ],
        id ='scrollable-column',
        style={
        'overflow-y': 'auto',
        'height': '80vh',
        'border': '1px solid #ddd',
        'padding': '15px',
        'background-color': '#ffffff',
        'border-radius': '5px',
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'marginBottom': '0px',
        'paddingBottom': '0px'
    })

    return instruction
