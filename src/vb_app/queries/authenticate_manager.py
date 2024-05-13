from MySQLdb import DatabaseError
from django.db import connection

#ALL SQL QUERIES ARE WRITTEN IN THIS FILE


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
    sql = "SELECT DISTINCT stadium_country, stadium_name FROM stadium"
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()  # fetch all the rows
            return rows
        except DatabaseError as e:
            print(f"Database error: {e}")
    return None  # Return None if query fails



def create_trigger_rate(): #jury can only rate a match if the date of the match has passed
    sql = """
    CREATE TRIGGER rate_trigger
    BEFORE INSERT ON assignedto
    FOR EACH ROW
    BEGIN
        DECLARE match_date DATE;
        SELECT date INTO match_date
        FROM playedin
        WHERE session_id = NEW.session_id;
        IF match_date > CURDATE() THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cannot rate a match that has not been played yet';
        END IF;
    END;
    """
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
        except DatabaseError as e:
            print(f"Database error: {e}")





