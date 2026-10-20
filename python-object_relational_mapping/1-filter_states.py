#!/usr/bin/python3
"""
and filters states starting with upper case N.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to MySQL server on localhost at port 3306.
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
    "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
