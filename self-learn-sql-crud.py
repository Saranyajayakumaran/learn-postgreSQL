from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Myfriends" table
class Myfriends(base):
    __tablename__ = "Myfriends"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    country = Column(String)
    postal_code = Column(Integer)

# instead of connecting to the database directly, we will ask for a session 
# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the session subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on Myfriends table
anitha_s = Myfriends(
    first_name="Anitha",
    last_name="s",
    gender="F",
    country="India",
    postal_code=12345
)

# add instance of friend to our session
session.add(anitha_s)

# commit the changes to the database
session.commit()

# query all records from Myfriends table
friends_list = session.query(Myfriends).all()

print("Column names:")
for friend in friends_list:
    print(
        friend.id,
        friend.first_name + " " + friend.last_name,
        friend.gender,
        friend.country,
        friend.postal_code,
        sep=" | "
    )

