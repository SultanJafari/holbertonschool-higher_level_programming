#!/usr/bin/python3
"""Prints the id of a State object by name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
