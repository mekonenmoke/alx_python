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
    mysql_username = "root"
    mysql_password = "0735"
    database_name = "hbtn_0e_0_usa"
    state_name = "Arizona"

    # Connect to the MySQL server
    try:
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

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()