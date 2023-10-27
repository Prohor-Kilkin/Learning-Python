import pickle
import os.path


class Model:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.title} - ({self.year}г.)"


class FilmsModel:
    def __init__(self):
        self.db_films = "Каталог фильмов.txt"
        self.movies = self.load_data()

    def add_movie(self, dict_film):  # {'название': qqq, 'автор': www}
        article = Model(*dict_film.values())  
        self.movies[article.title] = article

    def get_all_movies(self):
        return self.movies.values()

    def get_one_movie(self, film_title):
        movie = self.movies[film_title]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.genre,
            "год выпуска": movie.year
        }
        return dict_movie

    def del_movie(self, movie):
        return self.movies.pop(movie)

    def save_data(self):
        with open(self.db_films, "wb") as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.db_films):
            with open(self.db_films, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
