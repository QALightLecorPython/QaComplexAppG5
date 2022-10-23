"""DB samples using SQL alchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine(
    "mysql://root:1234@127.0.0.1:3306/storage_alch", echo=True
)
if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base()


class User(Base):
    """User rows description for 'users' table"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    password = Column(String(16))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<User('{self.name}', '{self.password}')>"


# Create table
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
session.add_all([User("Bejamin", "Benj1337"), User("Iren", "Dolores#1")])

# Select data
print("==============SELECT * FROM ========================")
for instance in session.query(User).order_by(User.id):
    print(instance.id, instance.name, instance.password)

# Insert data
vasiaUser = User("vasia", "vasia2000")
session.add(vasiaUser)

# Select data with filters
print("==============SELECT WITH FILTER ========================")
ourUser = session.query(User).filter_by(name="vasia").first()
print(ourUser.id, ourUser.name, ourUser.password)
