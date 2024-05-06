from django.db import connection


def authenticate_manager(username, password):
    sql="SELECT * FROM {table} WHERE username = %s AND password = %s "

    with connection.cursor() as cursor:
        cursor.execute(sql, [username, password])
        row = cursor.fetchone()  # Fetch the first row
        if row:
            return True
    return False  # Return None if authentication fails