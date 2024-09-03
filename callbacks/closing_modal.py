import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dashapp import app


@app.callback(
    Output('end_modal', 'is_open'),
    Input({'type': 'submit-survey', 'index': 4}, 'n_clicks'),
State('storage-general', 'data'),
)
def toggle_agree_button(submit_click, stored_data):
    print('Closing Screen Triggered!', submit_click)
    if stored_data.get('completed_pathways_maps', 'no') == 'yes' and submit_click > 0:
        return True
    else:
        False
