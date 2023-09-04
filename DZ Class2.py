import math


class Rectangle:

    def __init__(self, height, width):
        self.__height = self.__width = 0
        if Rectangle.__check_params(height) and Rectangle.__check_params(width):
            self.__height = height
            self.__width = width

    @staticmethod
    def __check_params(param):
        if type(param) in (int, float):
            return True
        else:
            return False

    def set_height(self, height):
        if Rectangle.__check_params(height):
            self.__height = height
        else:
            print("Неверный ввод.Введите числовое значения")

    def set_width(self, width):
        if Rectangle.__check_params(width):
            self.__width = width
        else:
            print("Неверный ввод.Введите числовое значения")

    def get_height(self):
        return f"Высота прямоугольника: {self.__height}"

    def get_width(self):
        return f"Ширина прямоугольника: {self.__width}"

    def calc_square(self):
        return f"Площадь равна: {self.__height * self.__width}"

    def calc_perimeter(self):
        return f"Периметр равен: {(self.__height + self.__width) * 2}"

    def calc_diagonal(self):
        return f"Диагональ равна: {math.isqrt(self.__height ** 2 + self.__width ** 2)}"

    def draw_rectangle(self):
        for i in range(self.__height):
            print("*" * self.__width)


r1 = Rectangle(10, 20)
r1.set_height(3)
r1.set_width(4)
print(r1.get_height())
print(r1.get_width())
print(r1.calc_square())
print(r1.calc_perimeter())
print(r1.calc_diagonal())
r1.draw_rectangle()

r2 = Rectangle(0, 0)
r2.set_height(12)
r2.set_width(25)
print(r2.get_height())
print(r2.get_width())
print(r2.calc_square())
print(r2.calc_perimeter())
print(r2.calc_diagonal())
r2.draw_rectangle()
