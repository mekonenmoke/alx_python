"""a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""
import MySQLdb

username = "root"
password = "0735"
name = "hbtn_0e_0_usa"

# create connection
connection = MySQLdb.connect(
    host="localhost", port=3306, user=username, password=password, db=name
)
curs = connection.cursor()

# execute query
curs.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")

# resultset
rows = curs.fetchall()
for row in rows:
    print(row)
