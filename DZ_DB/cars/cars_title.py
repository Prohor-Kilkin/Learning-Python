from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column
from DZ_DB.cars.database import Base


class Title(Base):
    __tablename__ = "title"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    models = relationship('Models')
