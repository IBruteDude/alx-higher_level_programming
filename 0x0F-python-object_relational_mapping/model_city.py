#!/usr/bin/python3
''' Module defining the sql tabled model of the City class '''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    ''' The declarative representation of the City class table '''
    __tablename__ = 'cities'
    id = Column(INT(), primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    state_id = Column(INT, ForeignKey("states.id"))
