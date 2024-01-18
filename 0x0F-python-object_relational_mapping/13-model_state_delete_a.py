#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter 'a'
from the MySQL database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py
<mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password>"
              "<database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Set up the connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query and delete State objects with a name containing 'a'
    deletel = session.query(State).filter(State.name.like('%a%')).all()
    for state in deletel:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
