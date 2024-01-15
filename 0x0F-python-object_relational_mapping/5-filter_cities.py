#!/usr/bin/python3
"""
Script to display all cities of a given state from the hbtn_0e_4_usa database.
Safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute a safe SQL query to retrieve cities of the specified state
    c.execute("SELECT * FROM `cities` as `c` "
              "INNER JOIN `states` as `s` ON `c`.`state_id` = `s`.`id` "
              "ORDER BY `c`.`id`")

    # Print the names of cities for the given state
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
