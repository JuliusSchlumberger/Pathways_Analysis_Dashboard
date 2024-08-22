# import dash
# from dash import dcc, html, Input, Output
# import dash_bootstrap_components as dbc
# import random
# from assets.static_inputs import WHICH_OPTIONS
# from dashapp import app
#
# # Update the dropdown based on the stored random value
# @app.callback(
#     Output('options', 'value'),
#     Output('options', 'options'),
#     Input('storage-general', 'data'),
#     Input('url', 'pathname'),
#     prevent_initial_call = True
# )
# def update_dropdown_value(stored_random_value,url):
#     if url == '/2-pathways-robustness':
#         options = [
#             {
#                 'label': label,
#                 'value': WHICH_OPTIONS[label],
#                 # 'disabled': WHICH_OPTIONS[label] != stored_random_value['robustness_plot']
#             }
#             for label in WHICH_OPTIONS
#         ]
#         return stored_random_value, options
#     else:
#         return dash.no_update, dash.no_update