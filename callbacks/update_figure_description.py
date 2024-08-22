import dash
from dash import Input, Output, State
from utilities.create_suited_question import *
from dashapp import app

@app.callback(
    [Output('dynamic-figure-paragraph', 'children'),
],
    Input('url', 'pathname'),
    Input('options', 'value'),
    prevent_initial_call=True
)
def update_paragraph(url, option):
    fig_description = html.P()

    if url == '/2-pathways-robustness':
        if option == None:
            fig_description = [
                html.P(
                    f"You need to select a figure type first."
                )
            ]
        elif option == 'PCP':
            fig_description = [html.Div([
                html.P(
                    "In this plot, each pathway corresponds to one polyline spanning a set of parallel axes, one for "
                    "each objective."),
                html.P(
                    "At each parallel axes you can select a range of acceptable values to filter out lines (pathways) "
                    "that do not meet this requirement. Double click on an axis with selected range resets the range."
                )
            ]
            )
            ]
        elif option == 'StackedBar':
            fig_description = [
                html.P(
                    "This figure adds overall the performance robustness of a pathways with regards to multiple "
                    "objectives by length. The shorter the bar, the higher the robustness. The length of each colored "
                    "bar for a given pathway is determined relative to the baseline scenario (when no measures are "
                    "implemented)."
                ),
            ]
        elif option == 'Heatmap':
            fig_description = [
                html.P(
                    "This figure uses colors to highlight relatively better performance robustness across multiple "
                    "objectives (y-axis) of different pathways (y-axis)."
                )
            ]
        return fig_description
    return dash.no_update
