"""a script that lists all states from the database
"""
import MySQLdb

username = "root"
password = "0735"
name = "hbtn_0e_0_usa"
# Connect to the MySQL server
connection = MySQLdb.connect(
    host="localhost", port=3306, user=username, password=password, db=name
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
