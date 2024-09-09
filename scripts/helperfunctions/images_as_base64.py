import base64
import plotly.graph_objects as go
import os

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return 'data:image/png;base64,' + encoded_string