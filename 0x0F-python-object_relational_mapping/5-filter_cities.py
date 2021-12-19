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
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id=\
                cities.state_id WHERE states.name LIKE BINARY %s \
                    ORDER BY cities.id", (argv[4], ))
    row = cur.fetchall()
    result = [i[0] for i in row]
    print(', '.join(result))
    cur.close()
    db.close()
