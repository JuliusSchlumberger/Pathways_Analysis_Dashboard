import pandas as pd
from sqlalchemy import create_engine

# Replace with your actual Heroku Postgres connection URL
DATABASE_URL = "postgresql://fsyzkozjzbneio:1dfc8383fa5c7bec0dc4e2abc9c3b14a07f9e9b9376129e4bba0f67960914625@ec2-52-72-109-141.compute-1.amazonaws.com:5432/d7usfk66t0qvat"

# Set up SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Query the database
query = "SELECT * FROM survey_responses"
df = pd.read_sql_query(query, engine)

# Export to CSV
df.to_csv('survey_responses.csv', index=False)
print("Data exported to survey_responses.csv")
