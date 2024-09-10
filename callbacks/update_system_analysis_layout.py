import dash
from dash import html, dcc, callback, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
from dashapp import app
from utilities.design_choices import TEXTFIELD_WIDTH, VIZ_STYLE_FIG, LAYOUT_HEIGHT
from assets.static_inputs import INTRO_TEXT, TIMEHORIZONS, SCENARIOS, WHICH_OPTIONS, ROBUSTNESS_METRICS, OPTION_DICT, INTERACTIONS, RANDOM_DEFAULT
from scripts.main_central_path_directions import ROH_LIST
from assets.static_inputs import ROH_DICT




# Define the layout
system_pathways_layout = dbc.Container(
    [
        # First row for header and Select elements

        dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Pathways and Measures Legend")),
                    dbc.ModalBody(id='modal_system_analysis-body'),  # Modal content will be dynamically updated here
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal", className="ms-auto", n_clicks=0)
                    )
                ],
                id="modal_system_analysis",  # Modal ID to control its visibility
                is_open=False,  # Initially not open
                className="modal-xl",
            ),
        # Second row for the graph
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="pathway-graph"), width=12
            )
        )
    ],
    fluid=True
)

system_performance_layout = dbc.Container(
    [
        dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Pathways and Measures Legend")),
                    dbc.ModalBody(id='modal_system_analysis-body'),  # Modal content will be dynamically updated here
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal", className="ms-auto", n_clicks=0)
                    )
                ],
                id="modal_system_analysis",  # Modal ID to control its visibility
                is_open=False,  # Initially not open
                className="modal-xl",
            ),
        # Second row for the graph
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="performance-graph"), width=12, style={'paddingLeft': '0', 'marginLeft': '0'}
            )
        )
    ],
    fluid=True
)



@app.callback(
    Output('system_analysis_focus_figure', 'children'),
    Output('system_analysis-graph', 'children'),
    Output('other_selection_options', 'children'),
    Output('store-page-E-selection', 'data', allow_duplicate=True),
    Output('system_analysis_focus', 'value'),
    Input('system_analysis_focus', 'value'),
    State('storage-general', 'data'),
prevent_initial_call=True
)
def set_up_layout(focus, stored_data):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('set_up_layout', triggered_id, stored_data)
    storage = {}
    if focus != None:
        storage['system_analysis_focus'] = focus
    else:
        storage['system_analysis_focus'] = stored_data.get('system_analysis_focus', None)
        focus = stored_data.get('system_analysis_focus', None)

    if focus == 'system_performance':
        selection_options = [html.Div([
                html.Label('b) Timehorizon for Evaluation', className='mb-1'),
                dbc.Select(
                    id='timehorizon',
                    options=[{'label': option, 'value': TIMEHORIZONS[option]} for option in TIMEHORIZONS],
                    value=stored_data['timehorizon']
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label('c) Climate Scenario', className='mb-1'),
                dbc.Select(
                        id='scenarios',
                        options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],
                    value=stored_data['scenarios']

                    )], style={'marginBottom': '20px'}),

            html.Div([
                html.Label('d) Robustness quantification', className='mb-1'),
                dbc.Select(
                        id='robustness_metric',
                    options=[{'label': option, 'value': ROBUSTNESS_METRICS[option]} for option in ROBUSTNESS_METRICS],
                    value=stored_data['robustness_metric']
                        # options=[{'label': option, 'value': ROBUSTNESS_METRICS[option], 'disabled': True if option != "mean across scenarios" else False
                        #     } for option in ROBUSTNESS_METRICS],
                        # value=list(ROBUSTNESS_METRICS.values())[0],
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label('e) Figure type', className='mb-1'),
                dbc.Select(
                    id='options',
                    # # Comment out the rest
                    options=[{
                            'label': RANDOM_DEFAULT,
                            'value': WHICH_OPTIONS[RANDOM_DEFAULT],
                        }
                    ],
                    value=stored_data['robustness_plot']
                    # value=random_default,  # Set the randomized value as the default
                ),
            ], style={'marginBottom': '20px'}),
            html.Div([
                html.Label(f'f) {list(ROH_DICT.keys())[0]} Pathways (select 2 or 3)'),
                dbc.Checklist(
                    id="pathway-1",
                    options=[
                        {"label": i, "value": i} for i in
                        range(0, 8)
                    ], value=[0,1], inline=True,
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label(f'g) {list(ROH_DICT.keys())[1]} Pathways (select 2 or 3)'),
                dbc.Checklist(
                    id="pathway-2",
                    options=[
                        {"label": i, "value": i} for i in
                        range(0, 8)
                    ], value=[0,1], inline=True,
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label(f'h) {list(ROH_DICT.keys())[2]} Pathways (select 2 or 3)'),
                dbc.Checklist(
                    id="pathway-3",
                    options=[
                        {"label": i, "value": i} for i in
                        range(0, 8)
                    ], value=[0,1], inline=True,
                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label(f'i) {list(ROH_DICT.keys())[3]} Pathways (select 2 or 3)'),
                dbc.Checklist(
                    id="pathway-4",
                    options=[
                        {"label": i, "value": i} for i in
                        range(0, 8)
                    ], value=[0,1], inline=True,
                )], style={'marginBottom': '20px'}),
            dbc.Row([
                dbc.Col(
                    dbc.Button('Update Figure',
                               id="show_figure_performance",
                               n_clicks=0
                               ),
                ),
            ],
                className="mb-3", style={'marginBottom': '0.1vh'}
            ),
        ]
        text = [html.P("This figure visualizes the robustness performance regarding objectives of multiple actor - risk pairs for selected combinations of pathways. "
                       "In the section above, select actor - risk pathways you want to consider in combination with other pathways. "
                       "Limit yourself to a maximum of 2 or 3 per actor, otherwise it gets very difficult to see."
                       "Use the button below to gain insight into the measures that are part of the selected pathways. "),
                dbc.Row([
                    dbc.Col(
                        dbc.Button('Show Legend',
                                   id="pathways-legend",
                                   n_clicks=0
                                   ),
                    ),
                ],
                    className="mb-3", style={'marginBottom': '0.1vh'}
                ),
                ]
        return text, system_performance_layout, selection_options, storage, focus
        # return system_performance_layout
    elif focus == 'system_pathways':
        selection_options = [
            html.Div([
                html.Label('b) Climate Scenario', className='mb-1'),
                dbc.Select(
                    id='scenarios',
                    options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],
                    value=stored_data['scenarios'],

                )], style={'marginBottom': '20px'}),
            html.Div([
                html.Label('c) Combination of Pathways', className='mb-1'),
                dbc.Select(
                    id="pathway-1",
                    options=[
                                {"label": f"{list(ROH_DICT.keys())[0]}: Pathway {i}", "value": i} for i in
                                range(1, 8)
                            ] + [{"label": f" {list(ROH_DICT.keys())[0]}: Not considered", "value": "not-considered"}],
                    value="not-considered", style={'marginBottom': '5px'}
                ),
                dbc.Select(
                    id="pathway-2",
                    options=[
                                {"label": f"{list(ROH_DICT.keys())[1]}: Pathway {i}", "value": i} for i in
                                range(1, 8)
                            ] + [{"label": f" {list(ROH_DICT.keys())[1]}: Not considered", "value": "not-considered"}],
                    value="not-considered", style={'marginBottom': '5px'}
                ),
                dbc.Select(
                    id="pathway-3",
                    options=[
                                {"label": f"{list(ROH_DICT.keys())[2]}: Pathway {i}", "value": i} for i in
                                range(1, 8)
                            ] + [{"label": f" {list(ROH_DICT.keys())[2]}: Not considered", "value": "not-considered"}],
                    value="not-considered", style={'marginBottom': '5px'}
                ),
                dbc.Select(
                    id="pathway-4",
                    options=[
                                {"label": f"{list(ROH_DICT.keys())[3]}: Pathway {i}", "value": i} for i in
                                range(1, 8)
                            ] + [{"label": f" {list(ROH_DICT.keys())[3]}: Not considered", "value": "not-considered"}],
                    value="not-considered", style={'marginBottom': '5px'}
                ),
                dbc.Row([
                    dbc.Col(
                        dbc.Button('Update Figure',
                                   id="show_figure_pathways",
                                   n_clicks=0
                                   ),
                    ),
                ],
                    className="mb-3", style={'marginBottom': '0.1vh'}
                ),
            ]
            ),

            ]

        text = [html.P("This figures represents a 'Metro-map' through time (starting at the left, moving to the right). "
               "You can select one pathway for each actor and risk. The respective pathway is highlighted in color. The full pathways map is shown for each actor - risk pair in grey. "),
        html.P("In case the colored line diverges from the grey pathways maps, this can be associated with the interaction with the other considered pathways."),
        html.P('You can select different combinations of pathways and observe changes with regards to the timing of the highlighted pathways'),
                dbc.Row([
                    dbc.Col(
                        dbc.Button('Show Legend',
                                   id="pathways-legend",
                                   n_clicks=0
                                   ),
                    ),
                ],
                    className="mb-3", style={'marginBottom': '0.1vh'}
                ),
                ]
        return text, system_pathways_layout, selection_options, storage, focus
    else:
        # Return empty divs or default values for all outputs
        return html.Div(), html.Div(), html.Div(), dash.no_update, dash.no_update

