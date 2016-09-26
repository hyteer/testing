from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

#Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
'''
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
'''
session.add_all([
   User(name='wendy', fullname='Wendy Williams', password='foobar'),
   User(name='mary', fullname='Mary Contrary', password='xxg527'),
   User(name='fred', fullname='Fred Flinstone', password='blah')]
)
session.commit()
#import pdb; pdb.set_trace()
#print dir(User.__table__)
