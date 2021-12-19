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
    cur.execute("SELECT * from states where name = '{:s}'".format(argv[4]))
    row = cur.fetchall()
    for i in row:
        if (i[1] == argv[4]):
            print(i)
    cur.close()
    db.close()
