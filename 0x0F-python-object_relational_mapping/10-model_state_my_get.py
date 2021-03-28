#!/usr/bin/python3
"""
Thing
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    check = 0
    engine_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                                  sys.argv[2],
                                                                  sys.argv[3])
    states_eng = create_engine(engine_url)

    obj = sessionmaker(states_eng)
    session = obj()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        if state.name == sys.argv[4]:
            print(state.id)
            check = 1
    if check == 0:
        print("Not found")
    session.close()
