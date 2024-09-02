from dash import dcc, html
import dash_bootstrap_components as dbc
from assets.static_inputs import PAGES

# Header with navigation links
header = dbc.Col(
    [
        dbc.Row(
            html.Div("Pathways Analysis Dashboard", className="me-2 bg-primary text-light", style={ 'font-size': '4.5vh','marginBottom': '.5vh',}),
            # align="center",  # Vertically center the content
            style={'marginLeft': '0.2vw', 'marginRight': '0.2vw', 'marginTop': '0.2vh', 'marginBottom': '0vw',
                   'paddingLeft': '0.2vw', 'paddingRight': '0.2vw', 'paddingTop': '0.2vh', 'paddingBottom': '0vw',
                   'height': '8vh'}
        ),
        dbc.Row(
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                # html.Div(style={'marginRight': '7vw',}),
                                *[item
                            for page in PAGES
                                for item in
                                  (html.Div(style={'borderLeft': '1px solid white', 'height': '80%'}),
                                      html.Div(page['title'], id=f"step-{page['step']}-link", style={'color': 'white', 'paddingTop': '1.vh', 'marginRight': '1vw','marginLeft': '1vw',  'font-size': '2.5vh'}),
                                html.Div(style={'borderLeft': '1px solid white', 'height': '80%'}))
                            ],],
                                width = 9,  # Distribute the PAGES over a width of 8
                                style = {'display': 'flex', 'alignItems': 'center', 'justifyContent': 'left'}
                                ),
                        dbc.Col([
                            dbc.Button("Back", id='prev-btn', n_clicks=0, color="secondary", className="ms-2",
                                           style={'height': '5vh', 'alignItems': 'center', 'font-size': '2.5vh'}),
                            dbc.Button("Next", id='next-btn', n_clicks=0, color="secondary", className="ms-2",
                                           style={'height': '5vh', 'alignItems': 'center', 'font-size': '2.5vh'}),
                            # dbc.Button("Resize", id='resize_screen', n_clicks=0, color="secondary", className="ms-2",
                            #                style={'height': '4vh', 'alignItems': 'center'}),
                            # style={'padding': '2vh'},
                            # width="auto"

                            ],
                            width=3,  # Place this button on the right in the remaining width of 2
                            style={'display': 'flex','alignItems': 'center', 'justifyContent': 'end'}
                        )
                    ],
                    justify="between",
                    style={'margin': '0px', 'padding': '0px', 'height': '6.8vh',}
                ),
                fluid=True
            ), className="bg-primary",
            style={'marginLeft': '0.4vw', 'marginRight': '0.4vw', 'marginTop': '0vh', 'marginBottom': '0vw',
                   'paddingLeft': '0.3vw', 'paddingRight': '0.3vw', 'paddingTop': '0vh', 'paddingBottom': '0vw'}
        ),
    ],
    style={
           'padding': '0px', 'height': '15vh', 'marginBottom': '.5vh'},
    width=12
)
