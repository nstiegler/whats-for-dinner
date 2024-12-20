import sqlite3
import os
from prettytable import PrettyTable 

def view_all_DBitems():
    # Explicitly define the database path
    db_path = "C:/Users/norma/GitHub/whats-for-dinner/whats_for_dinner.db"
    print(f"Using database file at: {db_path}")

    # Connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Query all rows in the 'meals' table
    c.execute("SELECT * FROM meals;")
    rows = c.fetchall()

    # Create a PrettyTable instance
    table = PrettyTable()

    # Set column names from the cursor description
    column_names = [description[0] for description in c.description]
    table.field_names = column_names

    # Add rows to the table
    for row in rows:
        table.add_row(row)

    # Close the database connection
    conn.close()

    return table


current_DBitems = view_all_DBitems()
print(current_DBitems)


def view_all_tables():
    conn = sqlite3.connect('whats_for_dinner.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)

    tables = cursor.fetchall()
    print("Tables in the DB")

    for table in tables:
        print(f"- {table[0]}")
    
db_tables = view_all_tables()
print(db_tables)