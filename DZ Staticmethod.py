import math


class Square:
    count = 0

    @staticmethod
    def counter():
        return f"Количество подсчетов площади: {Square.count}"

    @staticmethod
    def triangle_heron(a, b, c):
        p = (a + b + c) / 2
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Square.count += 1
        return f"Площадь треугольника по формуле Герона ({a},{b},{c}): {square}"

    @staticmethod
    def triangle_square(a, b):
        square = (a * b) / 2
        Square.count += 1
        return f"Площадь треугольника через основание и высоту ({a},{b}): {square}"

    @staticmethod
    def box_square(a):
        square = a ** 2
        Square.count += 1
        return f"Площадь квадрата ({a}): {square}"

    @staticmethod
    def rectangle_square(a, b):
        square = a * b
        Square.count += 1
        return f"Площадь прямоугольника ({a},{b}): {square}"


print(Square.triangle_heron(3, 4, 5))
print(Square.triangle_square(6, 7))
print(Square.box_square(7))
print(Square.box_square(7))
print(Square.rectangle_square(2, 6))
print(Square.counter())
