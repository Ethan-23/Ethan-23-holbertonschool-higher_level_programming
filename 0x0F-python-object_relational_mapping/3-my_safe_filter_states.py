#!/usr/bin/python3
"""
Things
"""
import MySQLdb
import sys

if __name__ == "__main__":
    states = MySQLdb.connect(user=sys.argv[1],
                             password=sys.argv[2],
                             host='localhost',
                             database=sys.argv[3],
                             port=3306)
    statesc = states.cursor()
    statesc.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = statesc.fetchall()
    for i in rows:
        if i[1] == sys.argv[4]:
            print(i)
    statesc.close()
    states.close()
