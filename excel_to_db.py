import pandas as pd
from sqlalchemy import create_engine

# Define your database connection string
DATABASE_URI = 'mysql://root:password@127.0.0.1:3308/db'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Sample Data - Project3.xlsx', sheet_name='MatchSession',usecols=['session_ID','assigned_jury_username','rating'])

#df= pd.read_excel('Sample Data - Project3.xlsx', sheet_name='MatchSession',usecols=['stadium_ID', 'stadium_country','stadium_name'])
#change column name played_player to player_username 
#df.rename(columns={'played_player_username':'player_username'}, inplace=True) 
#convert date to the format d-m-y
#df['contract_start'] = pd.to_datetime(df['contract_start'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d') 
#df['contract_finish'] = pd.to_datetime(df['contract_finish'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')

#df = df.drop_duplicates() #eğer primary keye sahip birden fazla aynı satır varsa onları siliyoruz

# Connect to your database using SQLAlchemy
engine = create_engine(DATABASE_URI)

df.to_sql('vb_app_assignedto', con=engine, if_exists='append', index=False)


# Player to vb_app_players
# Coach to vb_app_coaches
# Jury to vb_app_juries
# Position to vb_app_position
# PlayerPositions to vb_app_playerpositions but position column must be position_id 

