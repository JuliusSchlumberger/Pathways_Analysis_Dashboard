from dashapp import app
from dash import Input, Output

#
# # Callback to control the visibility of the text input based on selection
# @app.callback(
#     Output('self-describe-input', 'style'),
#     [Input('gender-radio', 'value')]
# )
# def toggle_self_describe_input(selected_value):
#     if selected_value == 'Prefer to self-describe':
#         return {'display': 'block'}
#     else:
#         return {'display': 'none'}

# Callback to control the visibility of the text input based on selection
@app.callback(
    Output('self-describe-input_visual', 'style'),
    Input('impairment-radio', 'value'),
    prevent_initial_call=True
)
def update_impairment_input(selected_value):
    if selected_value == 'Yes':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
