import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app

import dash
from dash import dcc, html, Input, Output, State, callback_context
import plotly.graph_objects as go
import plotly.io as pio

# @app.callback(
#     Output('dummy-div', 'children'),  # Dummy output, not used
#     Input('viewport-size', 'data')
# )
# def print_viewport_sizes(data):
#     # if data is not None:
#     vh_in_pixels = data['vh']
#     vw_in_pixels = data['vw']
#     print(f"Viewport Height: {vh_in_pixels} pixels, Viewport Width: {vw_in_pixels} pixels")
#     return None  # Dummy return, as the output is not visible or used
