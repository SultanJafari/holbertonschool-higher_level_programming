import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1]  #username
        passwd=sys.argv[2]  #password
        db=sys.argv[3]      #database name
    )



    cur = db.cursor()
    cur.execute("")


    rows = cur.fetchall()
    for row in rows:
        print(row)



    cur.close()
    db.close()
