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
    statesc.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC;".format(sys.argv[4]))
    rows = statesc.fetchall()
    for i in rows:
            print(i)
    statesc.close()
    states.close()
