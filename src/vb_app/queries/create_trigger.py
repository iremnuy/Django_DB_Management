from MySQLdb import DatabaseError
from django.db import connection
import os,dotenv
from dotenv import load_dotenv

load_dotenv()


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



if __name__ == '__main__':
    create_trigger_rate()