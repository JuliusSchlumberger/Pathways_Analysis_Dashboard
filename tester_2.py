import dash
from dash import html, dcc, Input, Output, clientside_callback
import plotly.graph_objects as go
import json

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Store(id='viewport-size'),  # Hidden div to store the viewport size
    html.Div(id='output'),          # Output div to display the viewport size (for testing)
    dcc.Graph(id='dynamic-figure')  # Graph that will use the viewport size
])

# Clientside function to capture viewport size
clientside_callback(
    """
    function(trigger) {
        return JSON.stringify({
            width: window.innerWidth,
            height: window.innerHeight
        });
    }
    """,
    Output('viewport-size', 'data'),
    Input('viewport-size', 'n_intervals')
)


@app.callback(
    Output('dynamic-figure', 'figure'),
    Input('viewport-size', 'data')
)
def update_figure(viewport_data):
    print(viewport_data)
    if viewport_data:
        size = json.loads(viewport_data)
        print(size)
        width, height = size['width'], size['height']
        # Adjust figure dimensions based on the viewport size
        fig = go.Figure(data=[go.Bar(x=["A", "B", "C"], y=[1, 3, 2])])
        fig.update_layout(width=width*0.8, height=height*0.8)  # Example scaling
        return fig
    return go.Figure()


if __name__ == '__main__':
    app.run_server(debug=True)
