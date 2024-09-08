from assets.static_inputs import PAGES
import dash_bootstrap_components as dbc

def get_step_from_pathname(pathname):
    try:
        return int(pathname.split('/')[1][0])
    except (ValueError, IndexError):
        return 0


def create_page_design(current_step):
    link_texts = [page['title'] for page in PAGES]

    link_styles = [
        {'fontWeight': 'bold', 'color': '#FFD700',
         'textDecoration': 'underline'} if i == current_step else {'color': 'white', 'font-weight': 'bold'}
        for i in range(len(PAGES))
    ]

    return [
        html.Div(link_texts[i], style=link_styles[i])
        for i in range(len(PAGES))
    ]

def create_link_design(current_step):
    link_texts = [page['title'] for page in PAGES]

    link_styles = [
        {'fontWeight': 'bold', 'color': '#FFD700',
         'textDecoration': 'underline'} if i == current_step else {'color': 'white'}
        for i in range(len(PAGES))
    ]

    links = [page['url'] for page in PAGES]

    return [
        dbc.NavLink(link_texts[i], href=links[i], style=link_styles[i])
        for i in range(len(PAGES))
    ]