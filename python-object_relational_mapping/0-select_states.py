"""a script that lists all states from the database
"""
import MySQLdb


def list_states(username, password, database):
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
        host="localhost", port=3306, user=username, password=password, db=database
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor object
    cursor.close()

    # Close the connection
    connection.close()


if __name__ == "__main__":
    username = "root"
    password = "0735"
    db_name = "hbtn_0e_0_usa"
    list_states(username, password, db_name)
