#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = "root"
    mysql_password = "0735"
    db_name = "hbtn_0e_0_usa"
    state_name = "Arizona"

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        charset="utf8",
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close cursor and disconnect from the server
    cursor.close()
    db.close()
