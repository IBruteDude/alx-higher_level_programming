#!/usr/bin/python3
from sys import argv
''' Module demonstrating the use of the sqlalchemy database API '''
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
    session.query(State).filter(State.id.like(2)).first().name = 'New Mexico'
    session.commit()
    session.close()
