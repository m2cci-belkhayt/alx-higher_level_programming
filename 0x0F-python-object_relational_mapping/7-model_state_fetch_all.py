#!/usr/bin/python3
"""
Script to list all State objects from the hbtn_0e_6_usa database.
Usage: ./7-model_state_fetch_all.py <mysql username>
        <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects ordered by their IDs
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
