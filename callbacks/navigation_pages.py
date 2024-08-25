import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dashapp import app
from datetime import datetime
from assets.static_inputs import WHICH_OPTIONS
import uuid
import random
from assets.static_inputs import PAGES
from pages.A_introduction import layout_A
from pages.B_alternative_pathways import layout_B
from pages.C_pathways_robustness import layout_C
from pages.D_pathways_maps import layout_D
from pages.F_multi_risk_pathways import layout_F



def generate_session_id():
    # Current time with microseconds to ensure uniqueness as much as possible
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    # Generate a random UUID
    unique_id = str(uuid.uuid4())
    # Combine them
    session_id = f"{current_time}"
    return session_id

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


@app.callback(
    [
        Output('page-content', 'children'),
        *[Output(f"step-{i}-link", "children") for i in range(len(PAGES))],
        Output('url', 'pathname'),
        Output('storage-general', 'data'),
        Output('prev-btn', 'n_clicks'),
        Output('next-btn', 'n_clicks'),
        Output("progress_modal", "is_open"),
        # Output("close-progress", "n_clicks"),
    ],
    [
        Input('prev-btn', 'n_clicks'),
        Input('next-btn', 'n_clicks'),
        # Input("close-progress", "n_clicks"),
        Input('url', 'pathname'),
    ],
    [State('viewport-size', 'data'),
        State('storage-general', 'data'),
        State('url', 'pathname'),
        # State('viewport-size', 'data'),
    ],
    prevent_initial_call=False  # Prevent callback from triggering on initial load
)
def display_page(prev_clicks, next_clicks, url, viewport, storage, current_path):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('navigation pages - triggered callback:', triggered_id, )
    print(storage)
    if not ctx.triggered or triggered_id == None:
        page_names = create_page_design(0)
        # Fallback for no trigger, initial content
        return layout_A, *page_names, PAGES[0]['url'], storage, 0, 0, False

    step_content_dict = {
            0: layout_A,
            1: layout_B,
            2: layout_C,
            3: layout_D,
            # 4: layout_E,
            # 5: layout_F
        }

    # Manage landing page
    if (current_path == '/' and storage == {}) or triggered_id == 'viewport-size':
        print('# Manage landing page')
        new_url = '/0-introduction'
        link_names = create_link_design(0)
        content = layout_A
        storage = {'existing_id': generate_session_id(),
                   'viewport_size': viewport,
                   'current_url': new_url}
        return (content,
                *link_names,
                new_url,
                storage,
                0, 0, False)
    # # Manage if navigation via url
    if triggered_id == 'url':

        print('# Manage if navigation via url', url, storage['current_url'])
        current_step = get_step_from_pathname(url)
        previous_step = get_step_from_pathname(storage['current_url'])
        page_names = create_link_design(current_step)
        content = step_content_dict.get(current_step, layout_A)
        storage['current_url'] = url
        if storage.get(PAGES[current_step]['check'], 'no') == 'yes' or previous_step <= current_step:
            return content, *page_names, url, storage, 0, 0, False
        # elif modal_click > 0:
        #     return dash.no_update, *[dash.no_update] * len(
        #         page_names), dash.no_update, dash.no_update, 0, 0,  False, 0
        else:
            return content, *page_names, url, storage, 0, 0, True

    # Manage if navigation via buttons
    print('# Manage if navigation via buttons')
    current_step = get_step_from_pathname(current_path)
    print('triggered_id', triggered_id, current_step, prev_clicks, next_clicks, )
    page_names = create_page_design(current_step)
    if triggered_id == 'next-btn' and current_step < len(PAGES) - 1:
        if storage.get(PAGES[current_step]['check'], 'no') == 'yes':
            new_step = current_step
            new_step = current_step + 1
            new_url = PAGES[new_step]['url']
            storage['current_url'] = new_url
            if viewport is not None:
                storage['viewport_size'] = viewport
            print(new_url)

            # Select the correct layout based on the new step
            content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

            page_names = create_link_design(new_step)

            return content, *page_names, new_url, storage, 0, 0, False
        else:
            return dash.no_update, *[dash.no_update] * len(
                page_names), dash.no_update, dash.no_update, 0, 0, True
    if triggered_id == 'prev-btn' and current_step > 0:
        new_step = current_step
        new_step = current_step - 1

        new_url = PAGES[new_step]['url']
        storage['current_url'] = new_url
        if viewport is not None:
            storage['viewport_size'] = viewport
        print(new_url)

        # Select the correct layout based on the new step
        content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(new_step)

        return content, *page_names, new_url, storage, 0, 0, False
        # elif modal_click > 0:
        #     return dash.no_update, *[dash.no_update] * len(
        #         page_names), dash.no_update, dash.no_update, 0, 0, False

    if triggered_id == 'close-progress':
        current_step = get_step_from_pathname(current_path)
        print('triggered_id', triggered_id, current_step, prev_clicks, next_clicks, )
        page_names = create_page_design(current_step)
        content = step_content_dict.get(current_step, layout_A)
        return content, *page_names, url, storage, 0, 0, False
    return dash.no_update, *[dash.no_update] * len(PAGES), dash.no_update, dash.no_update, 0, 0, False
