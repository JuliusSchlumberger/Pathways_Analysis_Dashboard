import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

from components import survey
# from callbacks import to_store

dash.register_page(__name__, path='/alternative_pathways')


visualization = dbc.Col([
    dbc.Row(id='alternatives-graph', style={'alignItems': 'top'}),
    # dbc.Row(html.Img(id='alternatives-image', src='', style={'alignItems': 'center'}), style={'height': '20%'}),
], style={'display': 'flex', 'flexDirection': 'column', 'height': '100vh'}, width=8)


# Define the tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Explanation", tab_id="tab-explanation-alternative_pathways"),
        dbc.Tab(label="Survey \u26A0", tab_id="tab-survey-alternative_pathways",  id="survey-tab-alternative_pathways")
    ],
    id="tabs-alternative_pathways",
    active_tab="tab-explanation-alternative_pathways",
)


# Define the tab content
tab_content = html.Div(id="tab-content-alternative_pathways", style={'margin-top': '1vh'})


layout = dbc.Row(
    [dbc.Col([
        tabs,
        tab_content], width=4, style={'height': '90vh'}),
     visualization],
    style={'height': '90vh'}
)


