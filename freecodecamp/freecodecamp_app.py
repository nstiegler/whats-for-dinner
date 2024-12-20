import freecodecamp.freecodecamp_database as freecodecamp_database


# Add a record to the DB
    # freecodecamp_database.add_one_record("Laura", "Smith", "laura@smith.com")

# Delete a record from the DB
    # freecodecamp_database.delete_one_record('6')

# Add many records
    # new_records_list =  [
    #     ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
    #     ('Joshua', 'Raintree', 'joshua@raintree.com')
    # ]

    # freecodecamp_database.add_many_records(new_records_list)

# Return lookup values 
email_question = input("Which email would you like to look up?")
freecodecamp_database.email_lookup(email_question)


# Call function from the other file
    # freecodecamp_database.show_all()