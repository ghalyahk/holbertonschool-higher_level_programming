#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # create cursor
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch and print results
    for row in cursor.fetchall():
        print(row)

    # close cursor and database
    cursor.close()
    db.close()
