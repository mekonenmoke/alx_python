from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class GeneralProduct(Base):
    __tablename__ = "generalProduct"

    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        