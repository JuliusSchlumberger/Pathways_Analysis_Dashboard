from dash.dependencies import Input, Output, State, ALL, MATCH
import dash
from dashapp import app, TABLE_NAME
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dashapp import app
import json
import os
from utilities.get_navigation_bar_design import *
from assets.static_inputs import PAGES
from pages.A_introduction import layout_A
from pages.B_alternative_pathways import layout_B
from pages.C_pathways_robustness import layout_C
from pages.D_pathways_maps import layout_D
from pages.E_system_analysis import layout_E

DATABASE_URL = os.getenv('DATABASE_URL')

step_content_dict = {
            0: layout_A,
            1: layout_B,
            2: layout_C,
            3: layout_D,
            4: layout_E,
            # 5: layout_F
        }

DATABASE_URL = os.getenv('DATABASE_URL')

def save_response_to_db(DATABASE_URL, user_id, data):
    # Adjust the URL format if necessary
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    # Set up SQLAlchemy
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    class SurveyResponse(Base):
        __tablename__ = TABLE_NAME
        id = Column(Integer, primary_key=True)
        user_id = Column(String)
        data = Column(Text)

    session = Session()
    response = session.query(SurveyResponse).filter_by(user_id=user_id).first()
    if response:
        response.data = json.dumps(data)
    else:
        response = SurveyResponse(user_id=user_id, data=json.dumps(data))
        session.add(response)
    session.commit()
    session.close()

@app.callback(
    Output('storage-general', 'data'),
     Output('page-content', 'children', allow_duplicate=True),
        *[Output(f"step-{i}-link", "children", allow_duplicate=True) for i in range(len(PAGES))],
        Output('url', 'pathname', allow_duplicate=True),
        Output("progress_modal", "is_open", allow_duplicate=True),
        Output('end_modal', 'is_open'),
    [
        Input({'type': 'submit-survey', 'index': ALL}, 'n_clicks'),
    Input('store-page-A-selection', 'data'),
     Input('store-page-B-selection', 'data'),
     Input('store-page-C-selection', 'data'),
     Input('store-page-D-selection', 'data'),
     Input('store-page-E-selection', 'data'),
     Input('store-page-A-form', 'data'),
     Input('store-page-B-form', 'data'),
     Input('store-page-C-form', 'data'),
     Input('store-page-D-form', 'data'),
     Input('store-page-E-form', 'data'),
    Input('storage-navigation', 'data')
     ],
    State('storage-general', 'data'),
    prevent_initial_call=True
)
def update_storage_general(n, store_A_selection, store_B_selection, store_C_selection, store_D_selection,
                           store_E_selection, store_A_form, store_B_form, store_C_form, store_D_form, store_E_form,
                           storage_navigation, storage_general):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('before', triggered_id, storage_general)
    index = 100
    if triggered_id.startswith('{'):
        triggered_dict = json.loads(triggered_id)
        if 'index' in triggered_dict:
            index = triggered_dict['index']


    print(store_A_form)
    # Update the central storage with non-None values from each page store
    if storage_navigation:
        print('ef called')
        storage_general.update(storage_navigation)
        check_complete = None
    if store_A_selection:
        print('As called')
        storage_general.update(store_A_selection)
        check_complete = None
    if store_B_selection:
        print('bs called')
        storage_general.update(store_B_selection)
        check_complete = None
    if store_C_selection:
        print('cs called')
        storage_general.update(store_C_selection)
        check_complete = None
    if store_D_selection:
        print('ds called')
        storage_general.update(store_D_selection)
        check_complete = None
    if store_E_selection:
        print('es called')
        storage_general.update(store_E_selection)
        check_complete = None
    if store_A_form:
        print('af1 called')
        storage_general.update(store_A_form)
        check_complete = 'completed_introduction'
        end_modal = False
    if store_B_form:
        print('af called')
        storage_general.update(store_B_form)
        check_complete = 'completed_alternative_pathways'
        end_modal = False
    if store_C_form:
        print('bf called')
        storage_general.update(store_C_form)
        check_complete = 'completed_pathways_robustness'
        end_modal = False
    if store_D_form:
        print('cf called')
        storage_general.update(store_D_form)
        check_complete = 'completed_pathways_maps'
        end_modal = False
    if store_E_form:
        print('df called')
        storage_general.update(store_E_form)
        check_complete = 'completed_system_analysis'
        end_modal = True

    # try:
    #     save_response_to_db(DATABASE_URL, storage_general['existing_id'], storage_general)
    # except Exception as e:
    #     print(f"Error storing data: {e}")
    print(check_complete)
    if check_complete != None:
        print(storage_general)
        if storage_general[check_complete] == 'yes':
            current_step = get_step_from_pathname(storage_general.get('current_url', '/0-introduction'))
            new_step = min(current_step + 1, len(PAGES) - 1)

            new_url = PAGES[new_step]['url']
            storage_general['current_url'] = new_url

            # Select the correct layout based on the new step
            content = step_content_dict.get(new_step, layout_A)  # Default to layout_A in case of an invalid step

            page_names = create_link_design(new_step)

            print('after', triggered_id, storage_general)
            return storage_general, dash.no_update if index == 5 else content, *page_names, dash.no_update if index == 5 else storage_general['current_url'], False, end_modal
        else:
            return storage_general, dash.no_update, *[dash.no_update] * len(
                PAGES), dash.no_update, True, False
    else:
        return storage_general, dash.no_update, *[dash.no_update] * len(
            PAGES), dash.no_update, False, False