#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL server and retrieves data from the states table based on provided arguments.

    Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>
    """

    # Retrieve arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        password=mysql_password,
        db=database_name,
        port=3306,
    )
    cursor = db.cursor()

    # Create and execute the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
