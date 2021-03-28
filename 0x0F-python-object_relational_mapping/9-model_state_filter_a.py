#!/usr/bin/python3
"""
Thing
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                                  sys.argv[2],
                                                                  sys.argv[3])
    states_eng = create_engine(engine_url)

    obj = sessionmaker(states_eng)
    session = obj()
    states = session.query(State).filter(State.name.contains('a')\
    ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
