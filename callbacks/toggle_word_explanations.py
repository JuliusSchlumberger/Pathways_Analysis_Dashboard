import dash
from dash import html, dcc, callback, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
from dashapp import app


@app.callback(
    Output({"type": "modal", "index": MATCH}, "is_open"),
    [Input({"type": "modal-link", "index": MATCH}, "n_clicks"), Input({"type": "modal-close", "index": MATCH}, "n_clicks")],
    [State({"type": "modal", "index": MATCH}, "is_open")]
)
def toggle_word_explanations(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
