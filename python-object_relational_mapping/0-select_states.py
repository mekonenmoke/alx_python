"""a script that lists all states from the database
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Retrieve and display a list of states from a MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database.

    Returns:
        None
    """

    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost", port=3306, user="root", passwd="0735", db="hbtn_0e_0_usa"
    )

    # Create a cursor to execute queries
    cursor = connection.cursor()

    # Execute the query to retrieve states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
