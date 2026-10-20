#!/usr/bin/python3
"""
Module that connects to a MySQL database and displays all states
where name matches the argument from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to MySQL server on localhost at port 3306
    and searches for a specific state name using format.
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
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
