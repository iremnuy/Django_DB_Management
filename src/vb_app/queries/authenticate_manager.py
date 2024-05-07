from MySQLdb import DatabaseError
from django.db import connection


def authenticate_manager(username, password, table):
    sql = f"SELECT * FROM {table} WHERE username = %s AND password = %s"

    with connection.cursor() as cursor:
        try:
            cursor.execute(sql, [username, password])
            row = cursor.fetchone()  # Fetch the first row
            if row:
                return True
        except DatabaseError as e:
            print(f"Database error: {e}")
    return False  # Return False if authentication fails

#COACH ENDPOINTS

def see_stadiums():
    sql = "SELECT DISTINCT stadium_country, stadium_name FROM MatchSession"
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()  # fetch all the rows
            return rows
        except DatabaseError as e:
            print(f"Database error: {e}")
    return None  # Return None if query fails




"""
def add_match(stadium_country,stadium_name,date,time,time_slot,jury_name,jury_surname):


    
def delete_match(session_id):







        
def create_squads(player_names:list):

"""



