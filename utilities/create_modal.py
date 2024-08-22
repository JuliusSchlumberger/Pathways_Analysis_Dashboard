import dash_bootstrap_components as dbc
from dash import html
def create_modal(modal_id, title, body):
    """
    Create a modal dialog for displaying detailed information.

    Parameters:
    modal_id (str): The unique identifier for the modal.
    title (str): The title of the modal.
    body (str or html): The content to be displayed inside the modal.

    Returns:
    dbc.Modal: A Dash Bootstrap Components Modal component.
    """
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle(title)),
            dbc.ModalBody(body),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id={"type": "modal-close", "index": modal_id},
                    className="ml-auto",
                    color="secondary"  # Flatly secondary color for the button
                )
            ),
        ],
        id={"type": "modal", "index": modal_id},
        is_open=False,
        backdrop="static",  # Prevent closing by clicking outside
        centered=True,  # Center the modal
        size="lg"  # Set modal size to large
    )


def create_modal_with_image(modal_id, title, image_src, body_text):
    """
    Create a modal dialog for displaying detailed information, including an image and text.

    Parameters:
    modal_id (str): The unique identifier for the modal.
    title (str): The title of the modal.
    image_src (str): The source URL of the image to be displayed.
    body_text (str): The text content to be displayed inside the modal.

    Returns:
    dbc.Modal: A Dash Bootstrap Components Modal component.
    """
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle(title)),
            dbc.ModalBody(
                html.Div([
                    html.Img(
                        src=image_src,
                        style={
                            'maxWidth': '100%',  # Limits the image width to the modal width
                            'maxHeight': '50vh',  # Limits the image height to 50% of the viewport height
                            'display': 'block',  # Center the image
                            'margin': '0 auto',  # Center the image
                            'marginBottom': '15px'
                        }
                    ),
                    html.P(body_text)
                ])
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id={"type": "modal-close", "index": modal_id},
                    className="ml-auto",
                    color="secondary"  # Flatly secondary color for the button
                )
            ),
        ],
        id={"type": "modal", "index": modal_id},
        is_open=False,
        backdrop="static",  # Prevent closing by clicking outside
        centered=True,  # Center the modal
        size="lg"  # Set modal size to large
    )
