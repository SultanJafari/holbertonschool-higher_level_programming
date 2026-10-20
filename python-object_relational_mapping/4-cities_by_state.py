#!/usr/bin/python3
"""
Module that connects to a MySQL database and lists all cities
with their corresponding states from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to MySQL server on localhost at port 3306
    and retrieves cities joined with their states.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
