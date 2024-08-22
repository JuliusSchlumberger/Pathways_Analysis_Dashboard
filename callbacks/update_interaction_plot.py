# import dash
# from dash import html, dcc, callback, Input, Output, State
# import dash_bootstrap_components as dbc
# import plotly.io as pio
# import plotly.graph_objects as go  # Import Plotly's graph_objects module
# from utilities.generate_missing_message import generate_missing_input_message
# from assets.static_inputs import CUSTOM_HOVER
# from utilities.scale_figure import scale_figure
# from assets.static_inputs import CUSTOM_LEGEND_CHANGE
# from dashapp import app
# import json
#
#
#
#
# @app.callback(
#     [Output('interactions-graph', 'children'),
#     Output('storage-general', 'data',allow_duplicate=True),
#      Output('multi_sectoral_interactions', 'value'),
#      Output('interaction_plot_options', 'value')
#      ],
#     [Input('multi_sectoral_interactions', 'value'),
#         Input('interaction_plot_options', 'value'),
#     ],
#     [State('storage-general', 'data'),],
# prevent_initial_call=True
# )
# def update_interaction_graph(interacting_sectors, plot_option, stored_data):
#
#     if interacting_sectors is not None:
#         stored_data['interacting_sectors'] = interacting_sectors
#     if plot_option is not None:
#         stored_data['plot_option'] = plot_option
#
#     message = generate_missing_input_message(
#         ('Interacting sectors', stored_data.get('interacting_sectors', None)),
#         ('Plot option', stored_data.get('plot_option', None)),)
#
#
#     if message:
#         return [html.Div('Make Choices (left side of display), to show visualization.',
#                          style={'color': 'red', 'fontSize': '1vw', 'fontWeight': 'bold', 'marginTop': '20px',
#                                 'textAlign': 'center'})], dash.no_update, dash.no_update, dash.no_update,
#
#     # Assume we have necessary details in stored_data to generate the figure
#
#     interacting_sector_string = stored_data["risk_owner_hazard"] + '&' + '&'.join(stored_data['interacting_sectors'])
#     scenario_str = '&'.join(stored_data['scenarios']) if len(
#         stored_data['scenarios']) > 1 else stored_data['scenarios'][0]
#
#     if stored_data["plot_option"] == 'map':
#         figure_type = 'PathwaysMaps'
#         file_path = f'assets/figures/{figure_type}/' \
#                     f'{stored_data["risk_owner_hazard"]}/' \
#                     f'pathways_map_{stored_data["risk_owner_hazard"]}_{scenario_str}_combi_{interacting_sector_string}.json'
#
#         with open(file_path, 'r') as f:
#             fig = pio.from_json(f.read())
#
#         fig, scaled_height, scaled_width = scale_figure(fig, stored_data)
#         # Convert the figure to an HTML string
#         fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
#
#         # Custom JavaScript to be added
#         custom_js = CUSTOM_HOVER
#
#         # Append the custom JavaScript to the HTML string
#         fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"
#
#         return html.Div([
#             html.Iframe(srcDoc=fig_html_with_js,
#                         style={"width": f"{scaled_width + .1 * scaled_width}px", "height": f"{scaled_height + .1 * scaled_height}px", "border": "none"}
#                         )
#         ]), stored_data, stored_data[
#             'interacting_sectors'], stored_data['plot_option']
#
#     else:
#         figure_type = stored_data["robustness_plot"]
#         file_path = f'assets/figures/{figure_type}/' \
#                     f'{stored_data["risk_owner_hazard"]}/' \
#                     f'plot_{stored_data["timehorizon"]}_{scenario_str}_{stored_data["robustness_metric"]}_combi_{interacting_sector_string}.json'
#
#         with open(file_path, 'r') as f:
#             fig = pio.from_json(f.read())
#         fig, _, _ = scale_figure(fig, stored_data)
#
#         if figure_type == 'StackedBar':
#             # Convert the figure to an HTML string
#             fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
#
#             # Custom JavaScript to be added
#             custom_js = CUSTOM_LEGEND_CHANGE
#
#             # Append the custom JavaScript to the HTML string
#             fig_html_with_js = f"{fig_html}\n<script>{custom_js}</script>"
#
#             # Return the HTML content
#             return html.Div([
#                 html.Iframe(srcDoc=fig_html_with_js,
#                             style={"width": "100%",  # Ensure iframe width fills the parent
#                                    "height": "100%",  # Ensure iframe height fills the parent
#                                    "border": "none",  # Remove borders if not needed
#                                    "overflow": "hidden"  # Prevent scrollbars from appearing
#                                    }
#                             )])
#         else:
#             return [dcc.Graph(figure=fig, responsive=False)], stored_data, stored_data[
#                 'interacting_sectors'], stored_data['plot_option']
#
