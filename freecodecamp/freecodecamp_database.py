# 1 - Import libaries
import sqlite3

# 2 - Create the connection & DB
conn = sqlite3.connect('customer.db') # 'customer.db' is the name of the DB we newly created

# 3 - Create a cursor
c = conn.cursor() # this allows us to create the table

# 4.2 - Create a table 
'''
# ----> You only have to create the table once via gitbash / powershell 
c.execute("""CREATE TABLE customers (
        first_name text, 
        last_name text, 
        email text
)""") # 'customers' is the table name / everything within the second set of '()' are the column names followed by data type
'''

# Datatypes:
    # NULL
    # INTEGER
    # REAL
    # TEXT 
    # BLOB


# 4.2 - Add a value to the newly created table / one value at a time
'''
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")
print("You have added a new record to the 'customers' table")
'''

# 4.3 - Add value(s) to the newly created table / multiple values at once
'''
many_customers = [
        ('Wes', 'Brown', 'wes@brown.com'),
        ('Steph', 'Kuew', 'steph@kuewa.com'),
        ('Dan', 'Pas', 'dan@pas.com')         
         ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) 
print("You have added multiple records to the 'customers' table")
'''

# 4.4 - Query the DB (see what is in the DB)
## 4.4.1 - Get all records 
### ----> the '*' signifies that we are getting all columns from the table named 'customers' 
### ----> ('SELECT * FROM your_table') 
### c.fetchone()
### c.fetchmany(3)
### print(c.fetchall()) # the 'fetch' does't produce an output so you have to wrap it in a 'print()' in order to see it

## 4.4.2 - Get all records with each records PK
### ----> we can also add 'rowid,' to return the PK for each record
### ----> c.execute("SELECT rowid, * FROM customers")

## 4.4.3 - Search through all records and return a specific record 
### ----> if we want to return specific records we can use the 'WHERE' clause
### ----> c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")

## 4.4.4 - Return a group of records that meet a certain criteria
### ----> if we want to return records that meet a general criteria then we can use 'WHERE' & 'LIKE' 
### ----> c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'") # returning all the last names that start with 'Br' (% = wildcard / starts with 'Br' and ends with anything)
### ----> c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'") # returning any email address that end with 'codemy.com'
# c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")



'''
# 4.5 - Format results 
# print(c.fetchone()[2]) # you can use the index to only pull a certain item from a given record via 'fetchone'
items_db = c.fetchall()


print(f"\tNAME \t \t\t\t EMAIL") # column headers for the print out
for item in items_db:
    print(f"rowID = {item[0]} name = {item[1]} {item[2]} \t| email address = {item[3]}")


print(f"\tNAME \t \t\t\t EMAIL") # column headers for the print out
for item in items_db:
    print(item) 

'''

# 4.6 - Primary Keys
## ----> PKs are unique ID numbers that each record gets
## ----> the '*' signifies that we are getting all columns from the table named 'customers' 
## ----> ('SELECT * FROM your_table') 
## ----> we can also add 'rowid,' to return the PK for each record
# c.execute("SELECT rowid, * FROM customers")

# 4.7 - Where & LIKE clause (return a group of records that meet a certain criteria)
### ----> if we want to return records that meet a general criteria then we can use 'WHERE' & 'LIKE' 
### ----> c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'") # returning all the last names that start with 'Br' (% = wildcard / starts with 'Br' and ends with anything)
### ----> c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'") # returning any email address that end with 'codemy.com'

# 4.8 - Updating records 
'''
c.execute("""UPDATE customers SET first_name = 'John'
            WHERE rowid = 1
    """)
'''


# 4.9 - Deleting records
'''
c.execute("DELETE from customers WHERE rowid = 6")
'''

# 4.10 - Ordering results 
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# 4.11 - And/Or 
## ----> this allows you to add more conditions to the 'WHERE' clause 
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

# 4.12 - Limiting results
## ----> you might only want to return a certain number of results
# c.execute("SELECT rowid, * FROM customers LIMIT 2")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' LIMIT 2")

# 4.13 - Drop table (deleting an entire table)
# c.execute("DROP TABLE customers")


# 7 - Creating funcitons to add & show records for our app
def show_all():
    """
    _summary_
    Querying the DB to return of all the records
    """
    
    conn = sqlite3.connect('customer.db') # connect to the DB
    c = conn.cursor() # creat the cursor

    
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # commit the command
    conn.commit()
    # close the connection
    conn.close()


def add_one_record(first, last, email):
    """
    Add a record to an existing table

    Args:
        first (string): first name
        last (string): last name
        email (string): email address
    """
    
    conn = sqlite3.connect('customer.db') # connect to the DB 
    c = conn.cursor() # create the cursor

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    conn.commit() # commit the command
    conn.close() # close the connection 


# 8 - Creating functions to delete records for our app
def delete_one_record(id):
    """Delete a specific record based on the rowid

    Args:
        id (int): the record's PK
    """
    
    conn = sqlite3.connect('customer.db') # connect to the DB
    c = conn.cursor() # create the cursor

    c.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit() # commit the changes
    conn.close() # close the connection 


# 9 - Add many records to our application 
def add_many_records(list):
    """
    Add multiple records to the DB

    Args:
        list (list): a list of the new records to add
    """

    conn = sqlite3.connect('customer.db') # connect to the DB
    c = conn.cursor() # create our cursor

    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    conn.commit() # commit the changes
    conn.close() # close the connection
    

# 10 - Where clause function 
def email_lookup(email):
    """
    Return records with the same email address criteria

    Args:
        email (str): the email address of the records you want to return
    """

    conn = sqlite3.connect('customer.db') # connect to the DB
    c = conn.cursor() # create the cursor

    # query and print results
    c.execute("SELECT * from customers WHERE email = (?)", (email,))

    items = c.fetchall()

    for item in items:
        print(item)

    
    conn.commit() # commit the changes
    conn.close() # close the connection 