import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dash
from dash.dependencies import Input, Output, State


# Replace with your actual Heroku Postgres connection URL
DATABASE_URL = "postgresql://fsyzkozjzbneio:1dfc8383fa5c7bec0dc4e2abc9c3b14a07f9e9b9376129e4bba0f67960914625@ec2-52-72-109-141.compute-1.amazonaws.com:5432/d7usfk66t0qvat"

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class SurveyResponse(Base):
    __tablename__ = 'survey_responses'
    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    page = Column(String)
    data = Column(Text)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_response_to_db(session_id, page, data):
    session = Session()
    response = session.query(SurveyResponse).filter_by(session_id=session_id, page=page).first()
    if response:
        response.data = json.dumps(data)
    else:
        response = SurveyResponse(session_id=session_id, page=page, data=json.dumps(data))
        session.add(response)
    session.commit()
    session.close()

@app.callback(
    Output('interactions-container', 'children'),
    Input('submit-survey-interactions', 'n_clicks'),
    [State('age-input', 'value'), State('storage-general', 'data')]
)
def save_answers_interactions(n_clicks, age, session_id):
    if n_clicks > 0:
        data = {"age": age}
        save_response_to_db(session_id['existing_id'], "introduction", data)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('alternative_pathways-container', 'children'),
    Input('submit-survey-alternative_pathways', 'n_clicks'),
    [State('pathway_number-input', 'value'), State('f_resilient_crops-input', 'value'),
     State('long_term-input', 'value'), State('flexibility-level', 'value'), State('storage-general', 'data')]
)
def save_answers_alternatives(n_clicks, pathway_number, f_resilient_crops, long_term, flexibility, session_id):
    if n_clicks > 0:
        data = {
            "pathway_number": pathway_number,
            "f_resilient_crops": f_resilient_crops,
            "long_term": long_term,
            "flexibility": flexibility
        }
        save_response_to_db(session_id['existing_id'], "alternatives", data)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('pathways_performance-container', 'children'),
    Input('submit-survey-pathways_performance', 'n_clicks'),
    [State('color-input', 'value'), State('crop_loss-input', 'value'), State('performance-input', 'value'),
     State('tradeoff-input', 'value'), State('storage-general', 'data')]
)
def save_answers_performance(n_clicks, color, crop_loss, performance, tradeoff, session_id):
    if n_clicks > 0:
        data = {
            "color": color,
            "crop_loss": crop_loss,
            "performance": performance,
            "tradeoff": tradeoff,
        }
        save_response_to_db(session_id['existing_id'], "pathways_performance", data)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('interaction_effects-container', 'children'),
    Input('submit-survey-interaction_effects', 'n_clicks'),
    [State('measure_shift-input', 'value'), State('performance_change-input', 'value'),
     State('strong_tradeoffs-input', 'value'), State('strong_synergy-input', 'value'), State('storage-general', 'data')]
)
def save_answers_interactions(n_clicks, measure_shift, performance_change, strong_tradeoffs, strong_synergy, session_id):
    if n_clicks > 0:
        data = {
            "measure_shift": measure_shift,
            "performance_change": performance_change,
            "strong_tradeoffs": strong_tradeoffs,
            "strong_synergy": strong_synergy,
        }
        save_response_to_db(session_id['existing_id'], "interaction_effects", data)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

