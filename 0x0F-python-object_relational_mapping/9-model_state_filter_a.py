#!/usr/bin/python3
# Lists all State objects containing the letter 'a' from the MySQL database hbtn_0e_6_usa.
# Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Set up the connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query and display State objects containing the letter 'a', ordered by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
