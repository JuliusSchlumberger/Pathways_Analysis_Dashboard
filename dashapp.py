import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True, use_pages=False, external_stylesheets=[dbc.themes.FLATLY])
app.title = 'Pathways Analysis Dashboard'

TABLE_NAME = 'survey_start_september'