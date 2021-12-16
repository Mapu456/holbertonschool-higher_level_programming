#!/usr/bin/python3
"""Function to print states in asc order"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states ORDER BY states.id"
    )
    for name in cur:
        print(name)
