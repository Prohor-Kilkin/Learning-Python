import json


class Countries:
    data = {}

    @staticmethod
    def rewrite_dz_json():
        with open("dz_json", "w") as f:
            json.dump(Countries.data, f)

    @staticmethod
    def add_data(country, city):
        Countries.data.update({country: city})
        Countries.rewrite_dz_json()

    @staticmethod
    def del_data(key):
        Countries.data.pop(key)
        Countries.rewrite_dz_json()

    @staticmethod
    def find_data(key):
        res = Countries.data.get(key, "Такой страны нет")
        print(key, "-", res)

    @staticmethod
    def edit_data(key, value):
        Countries.data[key] = value
        Countries.rewrite_dz_json()

    @staticmethod
    def show_data():
        with open("dz_json", "r") as f:
            print(json.load(f))


while True:

    print("*" * 30)
    print('''Выбор действия:
            1- Добавление данных
            2- Удаление данных
            3- Поиск данных
            4- Редактирование данных
            5- Просмотр данных
            6- завершение работы''')
    x = int(input("Ввод: "))
    if x <= 0 or x > 6:
        print("Введите цифру от 1 до 6.")

    if x == 1:
        Countries.add_data(input("Страна:"), input("Столица:"))
        print("Данные добавлены:")
        Countries.show_data()
    elif x == 2:
        Countries.del_data(input("Введите страну для удаления: "))
        print('Данные удалены, остались такие страны:')
        Countries.show_data()
    elif x == 3:
        Countries.find_data(input("Введите страну:"))
    elif x == 4:
        Countries.edit_data(input("Страна:"), input("Столица:"))
        Countries.show_data()
    elif x == 5:
        Countries.show_data()
    elif x == 6:
        print("Программа завершена")
        break
