#!/usr/bin/python3
"""
Prints the State object with the specified name from the MySQL database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Set up the connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with the specified name
    state_to_search = sys.argv[4]
    result_state = session.query(State).filter_by(name=state_to_search).first()

    # Display the result
    if result_state:
        print(result_state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
