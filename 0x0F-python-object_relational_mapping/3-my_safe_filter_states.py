#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

def search_states_safe(username, password, database, state_name):
    """
    Displays all values in the states table where name matches the argument (safe from SQL injection).
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        search_states_safe(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
