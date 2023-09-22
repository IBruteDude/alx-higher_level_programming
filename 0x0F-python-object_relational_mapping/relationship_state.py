#!/usr/bin/python3
''' Module defining the sql tabled model of the State class '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    ''' The declarative representation of the State class table '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
    mysql_charset = 'latin1'
