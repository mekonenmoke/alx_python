"""a script that lists all states from the database
"""
import MySQLdb

con = MySQLdb.connect(user="root", password="0735", db="hbtn_0e_0_usa")
cur = con.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
