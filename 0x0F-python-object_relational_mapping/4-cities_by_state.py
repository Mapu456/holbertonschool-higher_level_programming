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
    cur.execute('select cities.id, cities.name, states.name from cities left join\
	states on cities.state_id = states.id order by cities.id asc')
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
