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
    statesc.execute("SELECT cities.state_id, cities.name, states.name FROM cities LEFT JOIN states ON\
    states.id = cities.state_id ORDER BY cities.id ASC;")
    rows = statesc.fetchall()
    for i in rows:
        print(i)
    statesc.close()
    states.close()
