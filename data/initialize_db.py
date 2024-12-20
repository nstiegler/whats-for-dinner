# import sqlite3
# import json

# ----------------------------------------------------------------------------------


# # -- Initializing the 'meals' table -- ##

# # create the 'meals' DB
# conn_meals = sqlite3.connect('meals.db')
# conn_meals.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key support
# c_meals = conn_meals.cursor() 

# create the 'meals' table 
# c_meals.execute("""CREATE TABLE meals (
#     meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     meal_name TEXT NOT NULL UNIQUE,
#     cuisine TEXT NOT NULL,
#     protein TEXT NOT NULL,
#     prep_time INTEGER NOT NULL CHECK(prep_time > 0),
#     cook_time INTEGER NOT NULL CHECK(cook_time > 0)               
# )""")

# # Commit and close the connection
# conn_meals.commit()
# conn_meals.close()


# # -- Initializing the 'meals' table v2-- ##
### --> I didn't execute this in the gitbash terminal the first time so I don't think the table was actually created

# import sqlite3

# try:
#     # Connect to the database
#     conn_meals = sqlite3.connect('meals.db')
#     conn_meals.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key support
#     c_meals = conn_meals.cursor()

#     # Create the 'meals' table
#     c_meals.execute("""
#     CREATE TABLE IF NOT EXISTS meals (
#         meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         meal_name TEXT NOT NULL UNIQUE,
#         cuisine TEXT NOT NULL,
#         protein TEXT NOT NULL,
#         prep_time INTEGER NOT NULL CHECK(prep_time > 0),
#         cook_time INTEGER NOT NULL CHECK(cook_time > 0),
#         ingredients TEXT NOT NULL DEFAULT 'Unknown',
#         attributes TEXT NOT NULL DEFAULT 'None'
#     )
#     """)
#     print("Meals table created successfully.")

# except sqlite3.Error as e:
#     print(f"Error creating table: {e}")
# finally:
#     conn_meals.commit()
#     conn_meals.close()




# ----------------------------------------------------------------------------------


# # -- Adding the two additional columns to the 'meals' table -- ## 

# # Connect to your database
# conn = sqlite3.connect('meals.db')
# c = conn.cursor()

# # Add the columns
# try:
#     c.execute("ALTER TABLE meals ADD COLUMN ingredients TEXT NOT NULL DEFAULT 'Unknown';")
#     c.execute("ALTER TABLE meals ADD COLUMN attributes TEXT NOT NULL DEFAULT 'None';")
#     conn.commit()
# except sqlite3.OperationalError as e:
#     print(f"Error: {e}")
# finally:
#     conn.close()


# ----------------------------------------------------------------------------------


## -- Check the table's current schema -- ## 

# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('meals.db')
# c = conn.cursor()

# # Query the schema of the 'meals' table
# c.execute("PRAGMA table_info(meals);")
# columns = c.fetchall()

# # Print the column details
# print("Schema of 'meals' table:")
# for column in columns:
#     print(column)

# conn.close()


# ----------------------------------------------------------------------------------

## -- Test Run: add one record and confirm -- ## 

## 1.1 - Add record
# import sqlite3

# conn = sqlite3.connect('meals.db')
# c = conn.cursor()

# # Insert sample data
# c.execute("""
# INSERT INTO meals (meal_name, cuisine, protein, prep_time, cook_time, ingredients, attributes)
# VALUES ('Spaghetti Bolognese', 'Italian', 'Beef', 15, 45, 'Pasta, Beef, Tomato Sauce', 'Hearty;Classic')
# """)

# conn.commit()
# print("Sample meal inserted successfully.")

# conn.close()

# ## 1.2 - Query newly added record
# import sqlite3

# conn = sqlite3.connect('meals.db')
# c = conn.cursor()

# # fetch all meals
# c.execute("SELECT * FROM meals;")
# rows = c.fetchall()

# print("The following are all the records currently in the db: ")
# for row in rows:
#     print(row)

# print(f"The ")

# conn.commit
# conn.close



# ----------------------------------------------------------------------------------


## -- Validate I can print data from JSON file in the VS Code terminal -- ## 

# import sqlite3
# import json
# import os

# # Get correct file directory
# json_path = os.path.join(os.getcwd(), 'data', 'mock_data', 'mealsv2.json')
# print(f"Looking for file at: {json_path}")

# # Validate access to the json file and print JSON data
# try:
#     with open(json_path, 'r') as f:
#         data = json.load(f)
#     print("JSON data loaded successfully:")
#     print(json.dumps(data, indent=4))  # Pretty print JSON
# except FileNotFoundError:
#     print("Error: The file was not found at the specified path.")
# except json.JSONDecodeError as e:
#     print(f"Error: Invalid JSON format. {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


# ----------------------------------------------------------------------------------


## -- Add the mock data to the table -- ## 
# import sqlite3
# import json 
# import os

# def add_many_records(records):
#     """
#     Add multiple meal records to the DB.

#     Args:
#         records (list of tuples): List of meal records to add.
#     """

#     conn = sqlite3.connect('meals.db') 
#     c = conn.cursor() 

#     # query excluding meal_id
#     c.executemany("""
#         INSERT INTO meals (meal_name, cuisine, protein, prep_time, cook_time, ingredients, attributes)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, records)

#     conn.commit() 
#     conn.close() 
#     print("Your records were uploaded successfully!!!?!!!")

# # load JSON data
# json_path = os.path.join(os.getcwd(), 'data', 'mock_data', 'mealsv2.json')

# with open(json_path, 'r') as f:
#         data = json.load(f)


# # prep data transfer
# records_to_insert = []
# for meal in data["meals"]:
#       meal_name = meal["meal_name"]
#       cuisine = meal["cuisine"]
#       protein = meal["protein"]
#       prep_time = meal["prep_time"]
#       cook_time = meal["cook_time"]
#       ingredients = ", ".join(meal["ingredients"]) # convert list into a comma seperated string
#       attributes = str(meal["attributes"]) # convert a dictonary into a string

#       # append as a tuple
#       records_to_insert.append((meal_name, cuisine, protein, prep_time, cook_time, ingredients, attributes))

# # insert data into db
# add_many_records(records_to_insert)


# View the contents of the table
# def view_table():
#     conn = sqlite3.connect('meals.db')
#     c = conn.cursor()

#     c.execute("SELECT * FROM meals;")
#     rows = c.fetchall()

#     for row in rows:
#         print(row)

#     conn.close
# conn = sqlite3.connect('meals.db')
# c = conn.cursor()

# c.execute("SELECT * FROM meals;")
# rows = c.fetchall()

# for row in rows:
#     print(row)

# conn.close


# ----------------------------------------------------------------------------------


# # -- Initializing the 'meal_pick_history' table -- ##

import sqlite3

try:
    # Connect to the database
    conn_meal_pick_history = sqlite3.connect('whats_for_dinner.db')
    conn_meal_pick_history.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key support
    c_meal_pick_history = conn_meal_pick_history.cursor()

    # Create the 'meal_pick_history' table
    c_meal_pick_history.execute("""
    CREATE TABLE IF NOT EXISTS meal_pick_history (
        pick_id INTEGER PRIMARY KEY AUTOINCREMENT,
        meal_id INTEGER NOT NULL,
        pick_date DATETIME NOT NULL,
        notes TEXT,
        FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
    )""")
    print("'Meal Pick History' table created successfully.")

except sqlite3.Error as e:
    print(f"Error creating 'meal_pick_history' table: {e}")
finally:
    print("Committing changes to the database.....")
    conn_meal_pick_history.commit()
    conn_meal_pick_history.close()
    print("Database connection closed.....") 

