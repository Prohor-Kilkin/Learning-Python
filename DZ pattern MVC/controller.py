from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()


def run():
    while self.view.user_input() != "q":
