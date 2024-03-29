#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa
    """
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
