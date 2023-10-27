from view import UserInterface
from model import FilmsModel


class Controller:
    def __init__(self):
        self.films_model = FilmsModel()
        self.user_interface = UserInterface()

    def run(self):
        while True:
            answer = self.user_interface.user_answer()
            self.check_user_answer(answer)
            if answer == "q":
                self.films_model.save_data()
                break

    def check_user_answer(self, answer):
        if answer == "1":
            movie = self.user_interface.add_film()
            self.films_model.add_movie(movie)
        elif answer == "2":
            movies = self.films_model.get_all_movies()
            self.user_interface.show_all_films(movies)
        elif answer == "3":
            movie = self.user_interface.get_film_title()
            try:
                movie1 = self.films_model.get_one_movie(movie)
            except KeyError:
                self.user_interface.wrong_user_answer(movie)
            else:
                self.user_interface.show_one_film(movie1)
        elif answer == "4":
            movie = self.user_interface.get_film_title()
            try:
                movie1 = self.films_model.del_movie(movie)
            except KeyError:
                self.user_interface.wrong_user_answer(movie)
            else:
                self.user_interface.del_film(movie1)

        else:
            self.user_interface.wrong_input_key()