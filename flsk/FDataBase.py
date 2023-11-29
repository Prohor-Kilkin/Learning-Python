import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM menu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_goods(self, title, price):
        try:
            self.__cur.execute("INSERT INTO goods VALUES(NULL, ?, ?)", (title, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления в базу данных" + str(e))
            return False
        return True

    def get_goods(self):
        sql = "SELECT * FROM goods"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []