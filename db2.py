import sqlite3

def describe_tables(database_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Query to fetch table information
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Loop through each table and describe its columns
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")

        # Query to fetch column information for the current table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        # Print column details
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            not_null = "NOT NULL" if column[3] else ""
            primary_key = "PRIMARY KEY" if column[5] else ""
            print(f"    {column_name} {data_type} {not_null} {primary_key}")

        print()  # Empty line between tables

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Example usage:
database_file = 'Database/store.db'
describe_tables(database_file)
