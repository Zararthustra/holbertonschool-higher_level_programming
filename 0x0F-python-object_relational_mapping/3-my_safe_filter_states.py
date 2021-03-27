#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the
argument safe from sql injection
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_search, ))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
