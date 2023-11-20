from dz.cars.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class Models(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, ForeignKey('title.title'))
    color = Column(String)
    price = Column(Integer)