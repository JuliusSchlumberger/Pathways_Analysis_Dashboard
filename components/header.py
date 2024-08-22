from dash import dcc, html
import dash_bootstrap_components as dbc
from assets.static_inputs import PAGES

# Header with navigation links
header = dbc.Col(
    [
        dbc.Row(
            html.H3("Pathways Analysis Dashboard", className="me-2 bg-primary text-light"),
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
                                dbc.Button("Back", id='prev-btn', n_clicks=0, color="secondary", className="ms-2",
                                           style={'height': '6vh'}),
                                dbc.Button("Next", id='next-btn', n_clicks=0, color="secondary", className="ms-2",
                                           style={'height': '6vh'}),
                                html.Div(style={'marginRight': '7vw',}),
                                *[item
                            for page in PAGES
                                for item in
                                  (html.Div(style={'borderLeft': '1px solid white', 'height': '80%'}),
                                      html.Div(page['title'], id=f"step-{page['step']}-link", style={'color': 'white', 'paddingTop': '1.vh', 'marginRight': '1vw','marginLeft': '1vw'}),
                                html.Div(style={'borderLeft': '1px solid white', 'height': '80%'}))
                            ],
                            # style={'padding': '2vh'},
                            # width="auto"

                            ],
                        width="auto",
                        style={'display': 'flex', 'alignItems': 'center'}
                    )
                    ],
                    justify="between",
                    style={'margin': '0px', 'padding': '0px', 'height': '7.5vh'}
                ),
                fluid=True
            ), className="bg-primary",
            style={'marginLeft': '0.3vw', 'marginRight': '0.3vw', 'marginTop': '0vh', 'marginBottom': '0vw',
                   'paddingLeft': '0.3vw', 'paddingRight': '0.3vw', 'paddingTop': '0vh', 'paddingBottom': '0vw',}
        )
    ],
    style={
           'padding': '0px', 'height': '17vh'},
    width=12
)
