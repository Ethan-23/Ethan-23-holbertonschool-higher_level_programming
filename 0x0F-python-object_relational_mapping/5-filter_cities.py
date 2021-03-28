#!/usr/bin/python3
"""
Things
"""
import MySQLdb
import sys

if __name__ == "__main__":
    temp = 0
    states = MySQLdb.connect(user=sys.argv[1],
                             password=sys.argv[2],
                             host='localhost',
                             database=sys.argv[3],
                             port=3306)
    statesc = states.cursor()
    statesc.execute("SELECT cities.name FROM states RIGHT JOIN\
    cities ON states.id=cities.state_id WHERE states.name=%s\
    ORDER BY cities.id ASC", (sys.argv[4],))
    rows = statesc.fetchall()
    for i in rows:
        print(i[0], end="")
        if i != rows[-1]:
            print(", ", end="")
        else:
            temp = 1
            print()
    if temp == 0:
        print()
    statesc.close()
    states.close()
