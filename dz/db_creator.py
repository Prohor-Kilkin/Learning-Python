from dz.cars.database import create_db, Session
from dz.cars.cars_title import Title
from dz.cars.car_models import Models


def create_database():
    create_db()
    load_data(Session())


def load_data(session):
    cars = ["BMW", "Ford", "Opel"]
    models = [{"model": "x5", "color": "black", "price": 1000},
              {"model": "mondeo", "color": "blue", "price": 2000},
              {"model": "insigma", "color": "red", "price": 3000}
              ]

    for item in cars:
        title = Title(title=item)
        session.add(title)

    for item in models:
        model = Models(model=item["model"])
        session.add(model)
        color = Models(color=item["color"])
        session.add(color)
        price = Models(price=item["price"])
        session.add(price)

    session.commit()
    session.close()