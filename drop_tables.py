from django.db import connection

def delete_tables():
    # List of table names to be deleted
    tables_to_delete = ['MatchSession']

    try:
        # Create a cursor object
        with connection.cursor() as cursor:
            # Iterate over the list of tables to be deleted
            for table_name in tables_to_delete:
                # Generate the SQL query to drop the table
                drop_query = f"DROP TABLE IF EXISTS {table_name};"

                # Execute the SQL query
                cursor.execute(drop_query)
                print(f"Table {table_name} deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to delete the tables
delete_tables()
