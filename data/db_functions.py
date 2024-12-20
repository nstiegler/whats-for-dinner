import sqlite3
import json


# Add multiple records to the DB
def add_multiple_records(data_list):
    """
    Intsert multiple records into the list

    Args:
        data_list (list of tuples): List of records, each as a tuple (meal_name, cuisine, protein, prep_time, cook_time).
    """
    try:
        # connect to the db
        conn = sqlite3.connect('meals.db')
        c = conn.cursor()

        c.executemany("INSERT INTO meals VALUES (?,?,?,?,?,?)", data_list)

        # save changes & notify success
        conn.commit()
        print(f"{len(data_list)} records succesfully added to the table")

    except sqlite3.Error as e:
        print(f"An error occured: {e}")

    finally:
        conn.close



def add_simplified_meals(file_path):
    """
    Reads JSON data from a file and inserts it into a simplified meals table.
    
    Args:
        file_path (str): Path to the JSON file containing meal data.
    """
    try:
        # Load JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)
            meals = data["meals"]

        # Connect to the database
        conn = sqlite3.connect('meals.db')
        c = conn.cursor()

        for meal in meals:
            # Flatten the ingredients into a comma-separated string
            ingredients = ", ".join(meal["ingredients"])
            # Convert attributes to a JSON string
            attributes = json.dumps(meal["attributes"])

            # Insert into the simplified meals table
            c.execute("""
                INSERT INTO meals (meal_name, cuisine, protein, prep_time, cook_time, ingredients, attributes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                meal["meal_name"],
                meal["cuisine"],
                meal["protein"],
                meal["prep_time"],
                meal["cook_time"],
                ingredients,
                attributes
            ))

        # Commit changes and notify success
        conn.commit()
        print(f"Successfully added {len(meals)} meals to the database.")

    except sqlite3.Error as e:
        print(f"An error occurred with the database: {e}")
    except json.JSONDecodeError as e:
        print(f"An error occurred with the JSON file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        conn.close()





