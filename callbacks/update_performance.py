from dashapp import app
import dash
from dash import dcc, html, Input, Output, State
import plotly.io as pio
import json
from utilities.generate_missing_message import generate_missing_input_message


@app.callback(
    [
        Output('performance-graph', 'children'),
        Output('storage-pathways_performance', 'data'),
        Output('timehorizon', 'value'),
        Output('scenarios', 'value'),
        Output('performance_metric', 'value'),
        Output('options', 'value')
    ],
    [
        Input('timehorizon', 'value'),
        Input('scenarios', 'value'),
        Input('performance_metric', 'value'),
        Input('options', 'value'),
        Input('viewport-size', 'data')
    ],
    [State('storage-pathways_performance', 'data'),
     State('storage-alternative_pathways', 'data'),]
)
def update_performance_graph(timehorizon, scenarios, performance_metric, options,viewport_data,  stored_data_performance, stored_data_alternatives):
    if all(input_value is not None for input_value in
               [timehorizon, scenarios, performance_metric, options]):   # if this is not empty
        stored_data_performance['timehorizon'] = timehorizon
        stored_data_performance['scenarios'] = scenarios
        stored_data_performance['performance_metric'] = performance_metric
        stored_data_performance['options'] = options
    else:
        stored_data_performance['timehorizon'] = timehorizon
        stored_data_performance['scenarios'] = scenarios
        stored_data_performance['performance_metric'] = performance_metric
        stored_data_performance['options'] = options
        message = generate_missing_input_message(
            ('Risk Owner - Hazard Pair', stored_data_alternatives.get('risk_owner_hazard', None)),
            ('Timehorizon', stored_data_performance.get('timehorizon', None)),
            ('Climate Scenarios', stored_data_performance.get('scenarios', None)),
            ('Performance Indicator', stored_data_performance.get('performance_metric', None)))
        if message:
            return [html.Div(message,
                             style={'color': 'red', 'fontSize': '20px', 'fontWeight': 'bold', 'marginTop': '20px',
                                    'textAlign': 'center'})], dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    # Assume we have necessary details in stored_data_performance to generate the figure
    scenario_str = '&'.join(stored_data_performance['scenarios']) if len(stored_data_performance['scenarios'])>1 else stored_data_performance['scenarios'][0]
    file_path = f'assets/figures/{stored_data_performance["options"]}/' \
                f'{stored_data_alternatives["risk_owner_hazard"]}/' \
                f'plot_{stored_data_performance["timehorizon"]}_{scenario_str}_{stored_data_performance["performance_metric"]}.json'

    with open(file_path, 'r') as f:
        fig = pio.from_json(f.read())

    current_width = fig.layout.width
    current_height = fig.layout.height
    if current_height != None and current_width != None:
        size = json.loads(viewport_data)
        width, height = size['width'], size['height']
        scale_factor = min(width / 1920, height / 927)  # Assuming 1920px is the standard width for full scale

        # Scale the dimensions
        scaled_width = current_width * scale_factor
        scaled_height = current_height * scale_factor
        fig.update_layout(
            width=scaled_width,
            height=scaled_height,
            autosize=False,  # Ensure that the size is set explicitly based on scaled dimensions
            title_font_size=18 * scale_factor,
            font_size=14 * scale_factor,
        )
        # Scale annotation font sizes
        if 'annotations' in fig.layout:
            new_annotations = []
            for annotation in fig.layout.annotations:
                if annotation.font:
                    new_size = annotation.font.size * scale_factor if annotation.font.size else 12
                else:
                    new_size = 12 * scale_factor  # Default font size if not set

                new_annotations.append(
                    annotation.update(
                        font=dict(
                            size=new_size
                        )
                    )
                )
            fig.update_layout(annotations=new_annotations)
    return [dcc.Graph(figure=fig, responsive=True)], stored_data_performance, stored_data_performance['timehorizon'], stored_data_performance['scenarios'], \
           stored_data_performance['performance_metric'], stored_data_performance['options']