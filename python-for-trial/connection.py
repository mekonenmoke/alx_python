from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker

path = "mysql+mysqldb://root:0735@localhost/ethiodb"
database = create_engine(path)

Session = session_maker(bind=database)
session = Session