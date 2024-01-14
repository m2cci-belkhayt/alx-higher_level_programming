#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def list_cities(username, password, database, state_name):
    """
    Lists all cities of a specific state from the database hbtn_0e_4_usa.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute a single query to fetch the required data
        query = """
                SELECT cities.id, cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
