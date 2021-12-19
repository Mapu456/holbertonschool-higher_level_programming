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
    cur.execute("SELECT states.id, states.name FROM states WHERE\
        ASCII(states.name) = 78 ORDER BY states.id")
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
