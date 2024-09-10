import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dashapp import app



# Callback to toggle the enable state of the 'Agree' button based on the checkbox
@app.callback(
    Output("close-termsconditions", "disabled"),
    Input("terms-check", "value")
)
def toggle_agree_button(checkbox_value):
    return len(checkbox_value) == 0  # Button is disabled if checkbox is not checked

# Callback to handle closing the modal and showing content
@app.callback(
    Output("termsconditions", "is_open"),
    Output("close-termsconditions", "n_clicks"),
    # Output("content", "style"),
    Input("close-termsconditions", "n_clicks"),
    Input("close-termsconditions", "disabled"),
    prevent_initial_call=True
)
def toggle_initial_agreement(n, close_disabled):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('terms and conditions', triggered_id)
    if n > 0 and close_disabled == False:  # submit activated
        return False, 1  # Hide modal and show content
    return True, 0  # Default state
    # print('terms and conditions')
    # if stored_data.get('accepted_toc', 'no') == 'yes':
    #     return False, 1, dash.no_update
    # else:
    #
    #     if n > 0 and close_disabled == False:   # submit activated
    #         stored_data['accepted_toc'] = 'yes'
    #         return False, 1, stored_data  # Hide modal and show content
    #     return True, 0, dash.no_update  # Default state

