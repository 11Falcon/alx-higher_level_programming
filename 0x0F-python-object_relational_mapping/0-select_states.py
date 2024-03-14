#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)
    sys.exit(1)
