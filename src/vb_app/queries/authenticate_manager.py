from django.db import connection


def authenticate_manager(username, password):
    sql="SELECT * FROM DBManager D WHERE D.username = %s AND D.password = %s "

    with connection.cursor() as cursor:
        cursor.execute(sql, [username, password])
        row = cursor.fetchone()  # Fetch the first row
        if row:
            return True
    return False  # Return None if authentication fails