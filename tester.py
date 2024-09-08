import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create a figure with subplots
fig = make_subplots(
    rows=2, cols=2,  # 2x2 grid of subplots
    subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"),  # Subplot titles
    vertical_spacing=0.1,
    horizontal_spacing=0.05
)

# Add traces to subplots
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name="Plot 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 5, 4], mode='lines', name="Plot 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name="Plot 3"), row=2, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 5, 4], mode='lines', name="Plot 4"), row=2, col=2)

# Define layout with Graph and Modal
app.layout = dbc.Container([
    dcc.Graph(id='main-plot', figure=fig, config={'displayModeBar': False}),  # Main plot
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Expanded Subplot")),
            dbc.ModalBody(dcc.Graph(id='modal-plot')),  # Placeholder for enlarged plot
        ],
        id='modal',
        size='xl',  # Large modal size
        is_open=False  # Initially modal is closed
    )
])


# Callback to open modal and display the clicked subplot
@app.callback(
    [Output('modal', 'is_open'), Output('modal-plot', 'figure')],
    [Input('main-plot', 'clickData')],
    [dash.dependencies.State('modal', 'is_open')]
)
def display_modal_on_click(clickData, is_open):
    if clickData:  # If a click event occurs
        # Extract subplot information (row and col) from the clickData
        point = clickData['points'][0]
        x = point['x']
        y = point['y']
        subplot_title = point['curveNumber']

        # Create a new figure (enlarged version of the clicked subplot)
        subplot_fig = go.Figure()

        # Add the clicked trace to the new figure
        subplot_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[y, y, y], mode='lines', name=f"Selected Plot"))

        # Update the layout of the new figure (optional customization)
        subplot_fig.update_layout(
            title=f"Enlarged Subplot {subplot_title + 1}",
            xaxis_title="X Axis",
            yaxis_title="Y Axis",
        )

        return not is_open, subplot_fig  # Open modal with updated figure

    return is_open, go.Figure()  # Keep modal closed if no click event


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
