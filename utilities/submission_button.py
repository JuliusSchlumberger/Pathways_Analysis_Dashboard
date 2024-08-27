from dash import html
import dash_bootstrap_components as dbc

def submit_answers(button_id, container_id):
    return [html.Button('Submit', id=button_id, n_clicks=0,className='btn btn-primary',  style={'display': 'inline'}),
            dbc.FormText(id=container_id),
            ]

