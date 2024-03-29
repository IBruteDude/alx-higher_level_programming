#!/usr/bin/python3
''' Module demonstrating the use of the sqlalchemy database API '''
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    host, port = "localhost", 3306
    user, password, database = argv[1], argv[2], argv[3]
    engine = create_engine(
        f"mysql://{user}:{password}@{host}:{port}/{database}"
    )
    session = Session(bind=engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    all_as = session.query(State).filter(State.name.like('%a%')).delete()
    # for a in all_as:
    #     session.delete(a)
    session.commit()
    session.close()
