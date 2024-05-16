from dash import html

def generate_missing_input_message(*inputs):
    missing_inputs = [input_name for input_name, input_value in inputs if input_value is None]
    if missing_inputs:
        return html.P([f"To show a figure here, please make sure to select parameters in the Explanation Tab to the right.",
                html.Br(),
               f"Missing parameter(s) for: {', '.join(missing_inputs)}.",
                html.Br(),
               f"Fill in the question in the Survey Tab afterwards."])
    return None
