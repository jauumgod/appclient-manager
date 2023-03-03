from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import *


Session = sessionmaker(bind=app)
Base = declarative_base()


session = Session()

#create
name = ""
email = ""
new_user = User(name=name, email=email)
session.add(new_user)
session.commit()

#read

users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email)

#update

user = session.query(User).filter_by(name=name).first()
user.email = email
session.commit()

#delete
user = session.query(User).filter_by(name=name).first()
session.delete(user)
session.commit()