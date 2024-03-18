#!/usr/bin/python3
"""listing all states with a name starting with upper N"""

import sys
import MySQLdb

if __name__ == '__main__':
    username, password, name = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ID DESC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
