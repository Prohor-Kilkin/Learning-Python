from math import pi
choice = int(input("Площадь какой фигуры вы хотите вычислить?\n1-Прямоугольник\n2-Треугольник\n3-Круг\n: "))


def rectangle_square():
	a = int(input("Введите длину прямоугольника: "))
	b = int(input("Введите ширину прямоугольника: "))
	print("Площадь прямоугольника: ", a * b)


def triangle_square():
	a = int(input("Введите длину основания: "))
	b = int(input("Введите высоту треугольника: "))
	print("Площадь треугольника: ", (a * b) / 2)


def circle_square():
	r = int(input("Введите радиус круга: "))
	print("Площадь круга: ", round(pi * (r * r), 2))


if choice == 1:
	rectangle_square()
elif choice == 2:
	triangle_square()
elif choice == 3:
	circle_square()
else:
	print("Неверный ввод")
