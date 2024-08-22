from dash import html

def create_highlighted_word(word, modal_id):
    """
    Create a highlighted word element that triggers a modal when clicked.

    Parameters:
    word (str): The word to be highlighted.
    modal_id (str): The unique identifier for the modal associated with the word.

    Returns:
    html.Span: A Dash HTML Span component styled as a clickable, highlighted word.
    """
    return html.Span(
        word,
        id={"type": "modal-link", "index": modal_id},
        style={
            "cursor": "pointer",
            "color": "#007bff",  # Flatly primary blue color
            "textDecoration": "underline",
            "fontWeight": "bold"
        },
        n_clicks=0
    )
