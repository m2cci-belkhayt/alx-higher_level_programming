#!/usr/bin/python3
# Prints the first State object from the MySQL database hbtn_0e_6_usa.
# Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>
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

    # Query the first State object, ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    
    # Close the session
    session.close()
