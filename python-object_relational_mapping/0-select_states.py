"""a script that lists all states from the database
"""
import MySQLdb


def list_states(username1, password1, db_name1):
    """
    Retrieve and display a list of states from a MySQL database.

    Args:
        username1 (str): MySQL username.
        password1 (str): MySQL password.
        db_name1 (str): Name of the database.

    Returns:
        None
    """

    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=username1, password=password1, db=db_name1
    )

    # Create a cursor to execute queries
    cursor = connection.cursor()

    # Execute the query to retrieve states
    query = """SELECT * FROM states ORDER BY id ASC"""
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
    username = "root"
    password = "0735"
    db_name = "hbtn_0e_0_usa"

    list_states(username, password, db_name)
