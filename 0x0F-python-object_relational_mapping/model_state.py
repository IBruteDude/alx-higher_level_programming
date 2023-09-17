#!/usr/bin/python3
''' Module defining the sql tabled model of the State class '''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    ''' The declarative representation of the State class table '''
    __tablename__ = 'states'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    mysql_charset = 'latin1'
