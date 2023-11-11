from DataBase.database import Base


class Student(Base):
    __tablename__ = "student"


    id = Column()