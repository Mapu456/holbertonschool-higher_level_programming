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
    cur.execute("select cities.name from cities where state_id = 3")
    row = cur.fetchall()
    lon = len(row)
    count = 0
    for i in row:
        if count == lon - 1:
            print("{}".format(i[0]), end='')
        else:
            print("{}, ".format(i[0]), end='')
            count += 1

    cur.close()
    db.close()
