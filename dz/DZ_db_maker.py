import os
from cars.database import DATABASE_NAME
from dz import db_creator

if __name__ == '__main__':
    is_created = os.path.exists(DATABASE_NAME)
    if not is_created:
        db_creator.create_database()