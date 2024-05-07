import dash
from app import app

from dash import dcc, html
from dash.dependencies import Input, Output, State
from ..pages import introduction, alternative_pathways, pathway_performance, measure_timing, interaction_effects

#
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/':
#         print('test')
#         return introduction.layout()
#     elif pathname == '/page-1':
#         return alternative_pathways.layout()
#     elif pathname == '/page-2':
#         return pathway_performance.layout()
#     elif pathname == '/page-3':
#         return measure_timing.layout()
#     elif pathname == '/page-4':
#         return interaction_effects.layout()
#     else:
#         # If no match, you can return a 404 page
#         return '404'