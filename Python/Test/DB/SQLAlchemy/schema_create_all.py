from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine

engine=create_engine("mysql+pymysql://root:111@192.168.198.128:3306/test2",echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(40))
    #email = Column(String(40))
    password = Column(String(40))

    def __init__(self, name,fullname,password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s,' %s',' %s')>" % (self.name,self.fullname,self.password)

Base.metadata.create_all(engine)
