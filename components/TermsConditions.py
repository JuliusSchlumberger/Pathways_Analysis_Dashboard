import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

TermConditions = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Terms and Conditions"), close_button=False),
        dbc.ModalBody(
            [
                html.P("Welcome to the Pathways Analysis Dashboard (PAD)!"),
                html.P(
                    "Interactive visualizations can empower stakeholders to explore complex data, make better decisions, "
                    "and build trust in those decisions. We have developed this dashboard based on scientific insights "
                    "to support the analysis of Adaptation Pathways in complex systems."
                ),
                # html.P(
                #     [
                #         "By participating in this 15 to 30-minute study, you'll help us validate the benefits of different "
                #         "visualization types and the overall dashboard design. The survey consists of three parts:",
                #         html.Br(),
                #         "1. A few questions about you and your experience with visualizations.",
                #         html.Br(),
                #         "2. Tasks for you to complete using different visual aids.",
                #         html.Br(),
                #         "3. Your feedback on these visual aids.",
                #     ]
                # ),
                html.P(
                    [
                        "This research is conducted as part of the HORIZON 2020 ",
                        html.A("MYRIAD-EU project", href="https://www.myriadproject.eu/", target="_blank"),
                        ". If you have any questions regarding this study or the project, please reach out to ",
                        html.A("julius.schlumberger@deltares.nl", href="mailto:julius.schlumberger @ deltares.nl"),
                        ".",
                        html.Br(),
                        "This research is a collaborative effort with Jeroen Aerts, Marleen de "
                        "Ruiter, Robert Šakić Trogrlić, Jung-Hee Hyun, Stefan Hochrainer-Stigler, and Marjolijn Haasnoot.",
                        html.Br(),
                        "We want to thank all 21 participants in our group discussions and semi-structured interviews along with the 54 participants of the survey to test the dashboard whose contribution was critical for meaningful research.",

                    ]
                ),

                html.P(
                    ["Findings from this research are published here: ",
                    html.A("https://doi.org/10.5194/egusphere-2024-3655", href="https://doi.org/10.5194/egusphere-2024-3655", target="_blank"),
                     html.Br(),
                     "The Python code used to develop this Dashboard can be found ",
                    html.A("on Github", href="https://github.com/JuliusSchlumberger/PathwaysAnalysis_Dashboard", target="_blank"),
                    ".",
                    ]
                ),

                # html.P(
                #     [
                #         html.B("By consenting to participate in this study, you confirm that:"),
                #         html.Ul(
                #             [
                #                 html.Li(
                #                     "You understand that you can ask questions about this research before participating by using the email address provided above."
                #                 ),
                #                 html.Li(
                #                     "You understand that participation is voluntary, and you have the right to withdraw at any time for any reason. Deleting already submitted data is challenging and requires you to contact the above email address and specify identifying characteristics of your data, despite full anonymization of the dataset."
                #                 ),
                #                 html.Li(
                #                     [
                #                         "You agree that personal information, particularly related to visual impairments, will be anonymized and processed in accordance with the ",
                #                         html.A(
                #                             "General Data Protection Regulation (GDPR).",
                #                             href="https://gdpr-info.eu/",
                #                             target="_blank",
                #                         ),
                #                     ]
                #                 ),
                #                 html.Li(
                #                     "You understand that anonymized data may be used in research outputs (e.g., publications, reports, web pages)."
                #                 ),
                #                 html.Li(
                #                     "You understand that the dashboard should be opened on a single screen. If you change the screen dimensions, please refresh the webpage to ensure proper visualization. Uncommon screen dimensions may result in distorted visualizations."
                #                 ),
                #             ]
                #         ),
                #         html.B(
                #             "If you have concerns about this research or how it is being conducted, you can contact "
                #             "bethcie.beta @ vu.nl. Before participating in this survey, please review the statements above. "
                #             "If you wish to participate, please tick the box to confirm your consent."
                #         ),
                #     ]
                # ),
                # dbc.Checklist(
                #     options=[
                #         {"label": "I agree to the terms and conditions", "value": 1}
                #     ],
                #     value=[],
                #     id="terms-check",
                #     switch=True,
                # ),
                html.Img(
                    src='assets/figures/Myriad_Logo_BlackText_ColourDots.png',
                    style={
                        'maxWidth': '20%',
                        'maxHeight': '50vh',
                        'display': 'block',
                        'margin': '15px auto',
                    }
                ),
            ]
        ),
        dbc.ModalFooter(
            dbc.Button(
                # "Agree",
                "Proceed",
                id="close-termsconditions",
                # className="ms-auto",
                size='xl',
                n_clicks=0,
                disabled=False,  # Initially disabled
            )
        ),
    ],
    className="modal-xl",
    id="termsconditions",
    is_open=True,  # Start with the modal open
    backdrop="static",  # Prevent closing by clicking outside the modal
    keyboard=False  # Prevent closing by pressing escape key
)
