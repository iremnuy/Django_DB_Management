import pandas as pd
from sqlalchemy import create_engine

# Define your database connection string
DATABASE_URI = 'mysql://root:password@127.0.0.1:3308/db'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Sample Data - Project3.xlsx', sheet_name='DBManager')

# Connect to your database using SQLAlchemy
engine = create_engine(DATABASE_URI)

# Insert the DataFrame into the database
df.to_sql('DBManager', con=engine, if_exists='append', index=False)
