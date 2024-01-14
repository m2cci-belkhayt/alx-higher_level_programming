#!/usr/bin/python3
# Retrieves and prints all State objects from the MySQL database hbtn_0e_6_usa.
# Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Establish a connection to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create an SQLAlchemy Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and display State objects, ordered by id
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
