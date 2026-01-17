#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
