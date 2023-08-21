#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        "localhost", user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306
    )
    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id == cities.id ORDER BY cities.id ASC"""
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
