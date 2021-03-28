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

    new = State()
    new.id = len(session.query(State).all()) + 1
    print(new.id)
    new.name = "Louisiana"
    session.add(new)
    session.commit()
    session.close()
