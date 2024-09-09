from dashapp import app
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH
from scripts.design_choices.main_dashboard_dropdowns import ROH_DICT
from scripts.main_central_path_directions import ROH_LIST


def generate_image_based_on_text(text):
    if 'not-considered' in text:
        return html.Div()  # No image if 'not-considered'
    print(f'assets/legends/{text}.png')
    return html.Img(
        src=f'assets/legends/{text}.png', style={'width': '80%', 'display': 'block', 'margin': '0 auto 0 0', 'alignItems': 'middle',})  # Placeholder image

@app.callback(
    Output("modal_system_analysis", "is_open"),  # Controls the visibility of the modal
    [Input("pathways-legend", "n_clicks"), Input("close-modal", "n_clicks")],
    [State("modal_system_analysis", "is_open")]
)
def toggle_modal(open_clicks, close_clicks, is_open):
    # Toggle the modal when either the open or close button is clicked
    if open_clicks or close_clicks:
        return not is_open
    return is_open


@app.callback(
    Output('modal_system_analysis-body', 'children'),  # Target the modal body to update its content
    Input('pathways-legend', 'n_clicks'),  # Trigger when the button is clicked
    State('storage-general', 'data')
)
def populate_modal(n_clicks, storage_data):
    # Step 1: Static content (First Row)
    header_row = dbc.Row(
        html.H5("The combination of the following pathway(s) is considered")
    )
    # Step 2: Actor-risk names (Second Row)
    actor_risk_names = list(ROH_DICT.keys())[:4]
    second_row = dbc.Row([
        dbc.Col(html.P(
            f"{name}: Pathway {storage_data.get(f'pathway_{ROH_DICT[name]}', 'Not Considered')}") if storage_data.get(
            f'pathway_{ROH_DICT[name]}', 'not-considered') != 'not-considered' else html.P(
            f"{name}: Not Considered"), width=3) for name in
        actor_risk_names
    ])

    # Step 3: Dynamic content based on storage_data (Third Row)
    third_row = dbc.Row([
    dbc.Col(
        generate_image_based_on_text(
            f"{ROH_LIST[0]}/uniform_color/{ROH_LIST[0]}_pathway_{storage_data.get(f'pathway_{ROH_LIST[0]}', 'not-considered')}_ylabel"
        ),
        width=3,  # Auto width for image as well
        style={'padding-left': '5px'}  # Adjust the padding to reduce space
    ) if storage_data.get(f'pathway_{ROH_LIST[0]}') != 'not-considered' else dbc.Col(html.P()),

    dbc.Col(
        generate_image_based_on_text(
            f"{ROH_LIST[1]}/uniform_color/{ROH_LIST[1]}_pathway_{storage_data.get(f'pathway_{ROH_LIST[1]}', 'not-considered')}_ylabel"
        ),
        width=3,  # Auto width for image as well
        style={'padding-left': '5px'}  # Adjust the padding to reduce space
    ) if storage_data.get(f'pathway_{ROH_LIST[1]}') != 'not-considered' else dbc.Col(html.P()),

    dbc.Col(
        generate_image_based_on_text(
            f"{ROH_LIST[2]}/uniform_color/{ROH_LIST[2]}_pathway_{storage_data.get(f'pathway_{ROH_LIST[2]}', 'not-considered')}_ylabel"
        ),
        width=3,  # Auto width for image as well
        style={'padding-left': '5px'}  # Adjust the padding to reduce space
    ) if storage_data.get(f'pathway_{ROH_LIST[2]}') != 'not-considered' else dbc.Col(html.P()),

    dbc.Col(
        generate_image_based_on_text(
            f"{ROH_LIST[3]}/uniform_color/{ROH_LIST[3]}_pathway_{storage_data.get(f'pathway_{ROH_LIST[3]}', 'not-considered')}_ylabel"
        ),
        width=3,  # Auto width for image as well
        style={'padding-left': '5px'}  # Adjust the padding to reduce space
    ) if storage_data.get(f'pathway_{ROH_LIST[3]}') != 'not-considered' else dbc.Col(html.P()),

])


    # Step 5: Default image (Fifth Row)
    fifth_row = dbc.Row(
        dbc.Col(html.Img(src='assets/legends/full_overview_legend_uniform_color.png', style={'width': '80%'}), width=12),
        style={'marginTop': '20px'}
    )

    # Combine all rows into one Div
    modal_content = html.Div([
        header_row,
        second_row,
        third_row,
        html.Br(),
        fifth_row
    ])

    return modal_content
