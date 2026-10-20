#!/usr/bin/python3
"""

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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    query_rows = cursor.fetchall()
    cities_list = [row[0] for row in query_rows]
    print(",".join(cities_list))
    cursor.close()
    db.close()
