import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc


PROGRESS_MODAL = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Fill in the survey before you can proceed"), close_button=True),
        dbc.ModalBody([

            html.P([
               "Please answer all the questions regarding the visualizations and survey before proceeding to the next step.",
            ]),
        ]
        ),
    ],
    className="modal-xl",
    id="progress_modal",
    is_open=False,  # Start with the modal open
    # backdrop="static",  # Prevent closing by clicking outside the modal
    keyboard=False  # Prevent closing by pressing escape key
)

FINAL_MODAL = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Thank you for participating in this study!"), close_button=True),
        dbc.ModalBody([

            # html.P([
            #    "Thank you for taking your time to participate in this study. "]),
            # html.P(["In case you want to receive a notification when the results of the study are publicly available, "
            #                     "please reach out to ",
            #                 html.A("julius.schlumberger@deltares.nl", href="mailto:julius.schlumberger @ deltares.nl"),
            #                 "."]),
            #             html.P(["Similarly, if you have other feedback or ideas regarding the Pathways Analysis Dashboard or the "
            #                 "visualizations used, feel free to share these via above email address. "
            #             ]),
            html.P([
               "Thank you for exploring this pathways analysis dashboard! "]),
            html.P(["In case you have feedback or ideas regarding the Pathways Analysis Dashboard or the "
                "visualizations used, please reach out to ",
                html.A("julius.schlumberger@deltares.nl", href="mailto:julius.schlumberger @ deltares.nl"),
                "."]),

            html.P("This research is a collaborative effort with Jeroen Aerts, Marleen de Ruiter, Robert Šakić "
                   "Trogrlić, Jung-Hee Hyun, Stefan Hochrainer-Stigler, and Marjolijn Haasnoot."),
            html.P("This research is supported by the European Union’s Horizon 2020 research and innovation "
                   "programme (grant no. 101003276) as part of the MYRIAD EU project. Part of the work has been "
                   "conducted during the IIASA Young Scientists Summer Program (YSSP).")
        ]
        ),
    ],
    className="modal-xl",
    id="end_modal",
    is_open=False,  # Start with the modal open
    # backdrop="static",  # Prevent closing by clicking outside the modal
    keyboard=False  # Prevent closing by pressing escape key
)