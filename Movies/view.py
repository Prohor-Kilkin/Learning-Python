def add_title(title):
    def wrap(func):
        def inner(*args):
            print(title.center(50, "="))
            res = func(*args)
            print("=" * 50)
            return res
        return inner
    return wrap


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def user_answer(self):
        print("Действия с фильмами:")
        print("1 - Добавление фильма"
              "\n2 - Каталог фильмов"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Добавление фильма:')
    def add_film(self):
        dict_film = {
            "название ": None,
            "жанр": None,
            "год выпуска": None,
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @add_title('Каталог фильмов:')
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    def get_film_title(self):
        film_title = input("Введите название фильма: ")
        return film_title

    @add_title('Просмотр определенного фильма')
    def show_one_film(self, movies):
        for key in movies:
            print(f"{key} фильма - {movies[key]}")

    @add_title("Удаление фильма")
    def del_film(self, film):
        print(f"Фильм {film} был удален")

    @add_title("ОШИБКА")
    def wrong_user_answer(self, user_answer):
        print(f"Фильма {user_answer} в каталоге нет")

    @add_title("ОШИБКА")
    def wrong_input_key(self):
        print("Неверный ввод, выберите вариант из списка.")