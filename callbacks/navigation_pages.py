
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State, ALL

from dashapp import app
from utilities.generate_session_id import generate_session_id
from utilities.get_navigation_bar_design import *
from assets.static_inputs import WHICH_OPTIONS

import random
from assets.static_inputs import PAGES
from pages.A_introduction import layout_A
from pages.B_alternative_pathways import layout_B
from pages.C_pathways_robustness import layout_C
from pages.D_pathways_maps import layout_D
from pages.E_system_analysis import layout_E

@app.callback(
    [
        Output('page-content', 'children'),
        *[Output(f"step-{i}-link", "children") for i in range(len(PAGES))],
        Output('url', 'pathname'),
        Output('storage-navigation', 'data'),
        Output('prev-btn', 'n_clicks'),
        Output('next-btn', 'n_clicks'),
        Output("progress_modal", "is_open"),
        Output('end_modal', 'is_open', allow_duplicate=True)

    ],
    [
        Input('prev-btn', 'n_clicks'),
        Input('next-btn', 'n_clicks'),
        Input('url', 'pathname'),

        # Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks')
    ],
    [State('viewport-size', 'data'),
        State('storage-general', 'data'),
        State('url', 'pathname'),
        # State('viewport-size', 'data'),
    ],
    prevent_initial_call='duplicate_initial'  # Prevent callback from triggering on initial load
)
def display_page(prev_clicks, next_clicks, url, viewport, stored_data, current_path):
    storage = {}
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('navigation pages - triggered callback:', triggered_id, current_path)
    print(stored_data)
    if not ctx.triggered or triggered_id == None:
        page_names = create_link_design(0)
        # Fallback for no trigger, initial content
        return dash.no_update, *[dash.no_update] * len(PAGES), dash.no_update, storage, 0, 0, False, False

    step_content_dict = {
            0: layout_A,
            1: layout_B,
            2: layout_C,
            3: layout_D,
            4: layout_E,
            # 5: layout_F
        }

    # Manage landing page
    if current_path == '/' or triggered_id == 'viewport-size':
        print('# Manage landing page')
        new_url = '/0-introduction'
        link_names = create_link_design(0)
        content = layout_A
        # stored_data = {'existing_id': generate_session_id(),
        #            'viewport_size': viewport,
        #            'current_url': new_url}
        if stored_data.get('existing_id', None) == None:
            storage['existing_id'] = generate_session_id()
        storage[ 'viewport_size']= viewport
        storage['current_url']= new_url
        print('landing page', storage)
        return (content,
                *link_names,
                new_url,
                storage,
                0, 0, False, False)

    # # Manage if navigation via url
    if triggered_id == 'url':
        storage['viewport_size'] = viewport
        print('# Manage if navigation via url', url, stored_data.get('current_url', None))
        to_page = get_step_from_pathname(url)
        from_page = get_step_from_pathname(stored_data.get('current_url', '/0-introduction'))
        print(PAGES[to_page]['check'], to_page)
        if stored_data.get(PAGES[from_page]['check'], 'no') == 'yes' or from_page >= to_page:
            page_names = create_link_design(to_page)
            content = step_content_dict.get(to_page, layout_A)
            storage['current_url'] = url
            return content, *page_names, storage['current_url'], storage, 0, 0, False, False
        else:
            return (
                dash.no_update, *[dash.no_update] * len(PAGES), storage['current_url'], dash.no_update, 0, 0, True, False)

    # Manage if navigation via buttons
    from_page = get_step_from_pathname(current_path)
    print('current page', from_page)
    if triggered_id == 'next-btn' and next_clicks > 0 and from_page <= len(PAGES) - 1:
        to_page = min(from_page + 1, len(PAGES) - 1)
        print('# Manage if navigation via buttons', PAGES[from_page]['check'], next_clicks)
        if stored_data.get(PAGES[from_page]['check'], 'no') == 'yes':
            new_url = PAGES[to_page]['url']
            storage['current_url'] = new_url
            if viewport is not None:
                storage['viewport_size'] = viewport

            # Select the correct layout based on the new step
            content = step_content_dict.get(to_page, layout_A)  # Default to layout_A in case of an invalid step
            page_names = create_link_design(to_page)
            if from_page == len(PAGES) - 1:
                print('test')
                return dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, dash.no_update, 0, 0, False, True
            else:
                print('testw')
                return content, *page_names, new_url, storage, 0, 0, False, False
        else:
            print('test4')
            return dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, dash.no_update, 0, 0, True, False
    if triggered_id == 'prev-btn' and prev_clicks > 0 and from_page > 0:
        print('# Manage if navigation via buttons')
        storage['viewport_size'] = viewport
        to_page = from_page - 1

        new_url = PAGES[to_page]['url']
        storage['current_url'] = new_url

        # Select the correct layout based on the new step
        content = step_content_dict.get(to_page, layout_A)  # Default to layout_A in case of an invalid step

        page_names = create_link_design(to_page)

        return content, *page_names, new_url, storage, 0, 0, False, False
    return dash.no_update, *[dash.no_update] * len(PAGES), dash.no_update, dash.no_update, 0, 0, False, False
