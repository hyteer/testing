

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
#engine=create_engine("mysql+pymysql://root:111@192.168.198.128:3306/test",echo=True)
#metadata=MetaData(engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(40))
    email = Column(String(80))
    password = Column(String(20))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', email='%s')>" %\
        (self.name, self.fullname, self.email)

import pdb; pdb.set_trace()

#metadata.create_all()
