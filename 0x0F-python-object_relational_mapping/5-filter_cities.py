#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_search = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id=states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (state_search, ))
    query_rows = cur.fetchall()

    for i in range(len(query_rows)):
        if i + 1 == len(query_rows):
            print(query_rows[i][0])
        else:
            print(query_rows[i][0], end=", ")

    cur.close()
    conn.close()
