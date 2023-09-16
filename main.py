# name = 'Elena'
# print("Hello,", name)
# age = 20
# print(age)
# a = 5.2
# print(a)
# print(id(a))
# print(type(a))
# a = "Hello"
# print(a)
# print(id(a))
# print(type(a))

# a = b = c = 1
# print(a, b, c)

# a, b, c = "Hello", 5, 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a  # 1
# a = b  # 2
# b = c  # 1
# print("a:", a)
# print("b:", b)

# print("строка \n символов")
# print('строка строка строка строка строка строка строка строка строка строка строка строка строка строка строка строка '
#       'строка строка строка строка строка ')
# print("D:\\folder\\     file.py \"file\"")

# s1 = "Hello"
# s2 = "World__"
# s3 = s1 + " " + s2
# print(s3 * 4)

# print(465456345634654564654564)
# print(4.65456345634654564654564)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 4)
# print(6 // 4)
# print(6 ** 2)
# print(6 % 4)

# num = 9753  # 4
# print(num)
# a = num % 10
# # print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# # print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# # print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# # print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num1 = 4321  # 432
# print(num1)
# res = num1 % 10 * 1000
# num1 = num1 // 10
# res += num1 % 10 * 100
# num1 = num1 // 10
# res += num1 % 10 * 10
# num1 = num1 // 10
# res += num1 % 10
# print(res)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3
# print(num)  # 12
#
# num *= 4  # комментарий
# print(num)  # 48

# a = 10
# b = 5
# print("a:", a)
# print("b:", b)
# # a, b = b, a
# a = a + b  # 3
# b = a - b  # 3 - 2 = 1
# a = a - b  # 3 - 1 = 2
# print("a:", a)
# print("b:", b)


# num1 = "2"
# num2 = '3'
# print(type(num1))
# print(type(num2))
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.8945))
# a = 3.8945
# a = round(a, 1)
# print(a)
# print(type(a))
#
# print(int(3.8945))
# print(round(3.8945, 3))


# num1 = "5.2"
# num2 = 10
# print(type(num1))
# print(type(num2))
# res = float(num1) + num2  # 5.2 + 10
# print(res)


# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print()
# print("Меня зовут", name, ". Мне", age, "лет.", end=" ", sep="--")
# print("Продолжение строки.")

# name = input("Введите имя: ")
# print("Hello, ", name, "!", sep="")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = input("Введите число: ")
# # power = input("Введите степень: ")
# # num = int(num)
# # power = int(power)
# res = num ** power
# # res = int(num) ** int(power)
# print("num", type(num))
# print(res)


# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)
#
# print(type(b1))

# False = "", 0, False, None

# print(bool("Python"))
# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False


# a = None
# print(a)
# print(a is None)
# a = 5
# print(a)

# print(5 < 2)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 > 9)  # True && False
# print(2 * 5 > 7 >= 4 + 3)  # True && True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# && - and
# || - or
# ! - not

# print(5 - 3 == 2 or 1 + 3 == 4)

# print(not 9 - 9)

# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")
#

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")

# a = input('Введите первую сторону треугольника')
# b = input('Введите вторую сторону треугольника')
# c = input('Введите третью сторону треугольника')
# if a == b == c:
#     print('Ваш треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Ваш треугольник равнобедренный')
# else:
#     print('Ваш треугольник разносторонний')

# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)  # 1 <= 3 <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# m = int(input('Введите номер месяца: '))
# # if m == 12 or 1 <= m <= 2:
# if m == 12 or m == 2 or m == 1:
#     print('Зима')
# elif 3 <= m <= 5:
#     print('Весна')
# elif 6 <= m <= 8:
#     print('Лето')
# elif 9 <= m <= 11:
#     print('Осень')
# else:
#     print('Ошибка ввода')


# month = int(input("Введите номер месяца: "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif month == 3 or month == 4 or month == 5:
#     print("Весна")
# elif month == 6 or month == 7 or month == 8:
#     print("Лето")
# elif month == 9 or month == 10 or month == 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон (0-9): "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print("Пароль не верен")

# day = 'вторник'
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# Тернарное выражение

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)


# a, b = 30, 40
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 30, 0
# print("На 0 делить нельзя" if b == 0 else a / b)
# print(a / b)
# print("Код ниже")

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:  # исключение
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки. Нельзя делить на 0")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выводится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")  # '2'
# m = input("Введите второе число: ")  # 'пять'

# try:
#     n = int(n)  # 2
#     m = int(m)  # 'пять'
# except ValueError:
#     n = str(n)   # '2'
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# итерация - один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# n = int(input("Укажите количество символов: "))
# # # i = 0
# # # while i < n:
# # #     print("*", end="")
# # #     i += 1
# while n > 0:
#     print("*")
#     n -= 1
# print("*" * n)

# print("*" * 5)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:  # 1 3 5
#     if a % 2:  # a % 2 == 1  # a % 2 != 0
#         res += a  # res = res + a
#     a += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
# print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if j % 2:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     тело цикла

# for i in "Hello!":
#     print(i)

# for color in 'red', 'blue', 'green':
#     print(color)

# for element in range(start, stop, step):
#                         (0, stop, 1)
#     тело цикла

# for i in range(5, 10, 2):
#     print(i, end=" ")
#
# print()
#
# i = 5
# while i < 100:
#     print(i, end=" ")
#     i += 10


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(11, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Done!")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = [letter for letter in "Hello"]
# print(a)

# num = [i for i in range(20) if i % 2 == 0]
# print(num)


# Список (list)
# nums = [8, 3, 4, 1, 9, "Hello", 2.5]
# #      [0, 1, 2, 3, 4,  5,       6]
# #      [-7,-6,-5,-4,-3, -2,     -1]
# print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[-1])
# # print(nums[3])
# # nums[3] = 256
# # nums[0] += 100
# # print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# b = list('Hello')
# print(b)
# print(type(b))

# n = list(range(2, 10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)

# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# a = [i * 3 for i in 'list']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)


# a = [0] * int(input("Кол-во элементов в списке: "))
# # print(a)  # [0, 0, 0]
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# a = ['один', 'два', 'три', 'четыре', 'пять']
#
# for i in range(len(a)):  # 0 1 2 3 4
#     print(a[i], end=" ")
# print()
# for el in a:  # один два три четыре пять
#     print(el, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов:", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Кол-во четных элементов:", k)
# print("Сумма нечетных элементов:", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# try:
#     a = int(input("Число от 1 до 99: "))
#     kop = a
#     if 1 <= a <= 99:
#         if 11 <= kop <= 14:
#             print(a, "копеек")
#         else:
#             kop = kop % 10
#             if kop == 1:
#                 print(a, "копейка")
#             elif 2 <= kop <= 4:
#                 print(a, "копейки")
#             else:
#                 print(a, "копеек")
#     else:
#         print("Число не соответствует заданному диапазону")
# except ValueError:
#     print("Вы ввели не число")

# import math
#
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# import math as m
#
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
#
# print(num2)
# print(num3)

# from math import ceil, floor
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num2)
# print(num3)

# from math import *
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num2)
# print(num3)

# import time

# sec = time.time()
# print(sec)
# local = time.ctime(787883562)
# print(local)
# res = time.localtime()
# print(res)
# print(res.tm_year)
# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# print(time.strftime("Сегодня %B %d, %Y", time.localtime(787883562)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(787883562)))

# print("Программа запустилась...")
# time.sleep(5)
# print("Программа завершилась")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("Время выполнения программы", finish - start, "секунд")

# Срезы: список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# a = s[4:0:-1]
# print(a)

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[0:1])
# # print(s[6:7])
# # print(s[3:4])
# # print(s[-3:])
# # print(s[4:1:-1])
# # print(s[2:5])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []
# print(s)
# del s[:]
# print(s)

# Методы списков
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([8, 9, 10])  # добавляет в список итерируемый объект (несколько элементов)
# print(s)
# s.extend("add")
# print(s)
# s.insert(5, 100)  # добавляет элемент в список, первый параметр - индекс, второй параметр - добавляемое значение
# print(s)
# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     if i in c:
#         continue
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)  # [2, 1, 4, 3]

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):  # 3
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3,5)
#     c.append(b[i])
# if len(b) > len(a):
#     for i in range(len(a)):  # 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3,5)
#         c.append(a[i])
# print(c)


# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# s.remove(0)  # удаляет первый найденный элемент из списка по заданному значению
# print(s)
# last = s.pop()  # удалил последний элемент из списка и вернул удаляемое значение
# print(last)
# print(s)
#
# last = s.pop(0)  # удалил элемент по заданному индексу
# print(last)
# print(s)
#
# s.clear()  # очищает список
# print(s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# print(s)
# num = s.count(5)  # считает кол-во заданных элементов в списке
# print(num)
# ind = s.index(0, 2)  # возвращает индекс первого найденного элемента по его значению, если значения нет ValueError
# print(ind)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#     s += a[i]
# print(s / k)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(30)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 2, 3]
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)

# s = [9, 7, 3, 8, 4, 2, 6]
# s.sort(reverse=True)  # сортировка (по умолчанию - по возрастанию, reverse=True - сортировка по убыванию)
# print(s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# s = [9, 7, 3, 8, 4, 2, 6]
# s.sort()
# print(s)
#
# s2 = [9, 7, 3, 8, 4, 2, 6]
# s3 = sorted(s2)
# print(s3)
# print(s2)

# Генерация случайных данных

# import random
# from random import *

# print(random())
# print(randint(5, 9))
# print(randrange(2, 9, 2))  # randrange(start,stop,step)
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(choice(city))
# print(choices(city, k=3))
#
# s = [55, 66, 77, 88, 99, 4, 7, 9, 4, 5, 6, 1, 2, 7, 3]
# # print(choice(s))
# print(choices(s, k=5))

# from random import randint
#
# a = [randint(50, 100) for i in range(10)]
# print(a)


# lst = [5, 3, 4, 2, 1, 8]
# print(len(lst))
# print(min(lst))
# print("Max:", max(lst))
# print(sum(lst))

# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# m = max(a)
# print("Max:", m)
# a.remove(m)
# a.insert(0, m)
# print(a)


# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# minim = min(a)
# print("Min:", minim)
# ind = a.index(minim)
# print(ind)
# del a[:ind]
# # b = a[ind:]
# # print(b)
# print(a)

# x = list('1a2b3c4d')
# print(x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# if not lst:  # len(lst) == 0
#     print("Список пустой")
#
# print(bool(lst))  # False

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# # c = a + b
# # print("Третий список:", c)
# # c = []
# # for i in range(n1):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(n2):
# #     if b[i] not in c:
# #         c.append(b[i])
# # print("Третий список:", c)
# # c = []
# # for i in range(n1):
# #     if a[i] in b and a[i] not in c:
# #         c.append(a[i])
# # print("Третий список:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Третий список:", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print()
# print(len(m))
# print(m[1][2])
# for row in range(len(m)):  # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, "=", x + y)
# from random import randint

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# from random import randint
# w, h = 3, 4
# s = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end="\t\t")
#     print()
#
# print(s)


# Функции
# print()
#
#
# def hello(name, word):  # аргументы
#     print("Say", word, "Hello", name)
#
#
# hello("Irina", "hi")  # параметры
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# n = 2
# m = 3
# get_sum(n, m)
# c = 5
# d = 6
# get_sum(c, d)


# def symbol(count, a, b):
#     for i in range(count):  # 012345678
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print("Текст")
#     return a + b
#
#
# n = 2
# m = 3
# res = get_sum(n, m)
# print(res)

# def add(x, y):
#     if x > y:
#         return x - y
#     return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print("Результат:", m)


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst


# def change(lst):
#     a = lst.pop()  # последний элемент
#     b = lst.pop(0)  # первый элемент
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 5
# b = 12
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Нет")
# p = input("Введите пароль: ")
#
#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:  # True and True
#         return True
#     return False
#
#
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Ненадежный пароль")


# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# n = 2
# m = 5
# print(get_sum(1, d=n, b=m))

# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()
# set_param(s="?")

# def digits_sum(n, even=True):  # n = 0
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 9
#         if even and cur_digit % 2 == 0:
#             s += cur_digit  # s = 14
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = 5
# print(a, id(a))
# a = 6
# print(a, id(a))
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])
# print(lst1, id(lst1))

# a = "Hello"
# b = "Hello"
# a = [1, 2, 3]
# b = [1, 2, 3]
# a = True
# b = True
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# Изменяемые типы данных - list, set
# Неизменяемые типы данных - int, str, float, bool, tuple

# st = "Hello"
# st = list(st)
# print(st[-1])
# st[-1] = 'q'
# print(st)

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = tuple((2, 5, 7, 9, 8))
# print(a)
# print(a[-1])
# print(a[1:3])

# s = tuple(input("=> ") for i in range(5))
# print(s)

# from random import randint
#
# s = tuple(randint(0, 10) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.index('l', 4))
# # print(t3.count('a'))
# # ch = 'w'
# # if ch in t3:
# #     print(t3.index(ch))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i * 2, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1) + 1  # 5
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# from random import randint


# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl_1 = ran(0, 5)
# tpl_2 = ran(-5, 0)
# print(tpl_1)
# print(tpl_2)
# tpl_3 = tpl_1 + tpl_2
# print(tpl_3)
# print("0 =", tpl_3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# del t[4][0]
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # n, year, married = user
# n, year, married = get_user()
# print(n, year, married)


# tpl = (10, 20, 30)
# del tpl
# print(tpl)

# tpl = (10, 20, 30)
# lst = list(tpl)
# lst.append(50)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ". Население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ". Население: ", city_population, sep="")

# Множество (set)
# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# for i in s:
#     print(i)

# a = set()
# print(a)
# print(type(a))

# s = {i * i for i in range(10)}
# print(s)
# print(64 not in s)


# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' not in i}
# # a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# print(a)
#
# for i in s:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print('B' + i[1:])

# a = {"Tom", "Bob", "Alice"}
# a.add("Sam")
# print(a)
# # a.remove("Tom")
# # a.remove("Ann")  # KeyError
# # print(a.pop())
# # a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # print(c)
# # c = a - b
# # print(c)
# c = a ^ b
# print(c)
# print(c)
# a |= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# [1, 2, 3, 4, 5]
# s = frozenset({i ** 2 for i in range(10)})
# print(s)

# Словари (dict)

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 3: 0}
# print(type(d))
# print(lst[0])
# print(d['one'])
# print(lst[2])
# print(d[3])

# d = {'one': 1, 'two': 2, 3: 0}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# users = [('a', 'b'), ['c', 'd'], ['e', 'f']]
# print(users)
# d_users = dict(users)
# print(d_users)
# lst = list(d_users)
# print(lst)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20 * 2
# print(d)
# s = {0, 1, 2, 0}
# print(s)
# s.remove(3)
# print(s)
# d = {0: 'text', 'one': 1, (1, 2.3): 'кортеж', 2: [5, 7, 8, 9], True: 1, False: 9}
# print(d)
# print(d[(1, 2.3)])
# print(d[2][1])
# print('one' in d)
# del d[0]
# print(d)
# print(d['one1'])
# lst = [1, 2, 3]
# print(lst[3])

# d = {'one': 1, 'two': 2, 'three': 3}
#
# # for key in d:
# #     print(key, d[key])
# # key = 'two'
# # if key in d:
# #     del d[key]
#
# key = 'three'
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
#
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()  # {}
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# # dislike = int(input("Какой элемент исключить: "))
# del d[int(input("Какой элемент исключить: "))]
# print(d)

# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(len(d))
# print(max(d))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input("Количество: "))
#         goods[n][1] += k
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений
# # for i, j in d.items():
# #     print(i, j)
#
# print(set(d))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
#
# d2['b'] = 5
# d['e'] = 7
#
# print("D =", d)
# print("D2 =", d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.update({'a': 7, 't': 9})  # обновление словаря
# d.update([('b', 5), ('q', 7)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.clear()  # очистить словарь
# # item = d.pop('b', 'Такого ключа нет')  # удаляет ключ и значение по ключу, возвращает значение
# item = d.popitem()  # удаляет ключ и значение последние в словаре, возвращает кортеж из удаляемых элементов
# print(item)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # new_d = dict()
#
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
#
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# s = dict()
# n = None
#
# for i in a:  # 1
#     if type(i) == str:
#         s[i] = []  # s['two'] = []
#         n = i  # n = 'two'
#     else:
#         s[n].append(i)  # s['two'] = [10, 20]
#
# print(s)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# s = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(s)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {v: k for k, v in zip(a, b)}
# print(f)


# a = [1, 2, 3, 4, 5]
# c = [4.0, 8.5, 9.4]
# d = ['a', 'b']
# b = list(zip(a, c, d))
# print(b)

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': "Consultant"}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': "Manager"}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# two = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*two)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})  # {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}

# s = ['red', 'blue', 'green']
# # j = 1
# for j, i in enumerate(s, 1):
#     print(j, ") ", i, sep="")
# j += 1


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 2, 4))
# print(func())


# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(3, 4, 5))
# print(summa('a', 'b'))


# def ch(*args):
#     average = sum(args) / len(args)
#     print("Среднее арифметическое:", average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 8, 7, 8, 9, 4, 5, 6, 1))

# def print_scores(student, *scores):
#     print("Student:", student, end=": ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())


# def info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#
#
# info(name="Irina", surname="Sharma", age=22, phone=1234567890)
# info(name="Igor", surname="Wood", email='igor@gmail.com', country="Russia", age=25, phone=6781234590)


# def func(a, n, m, *args, d=1, r=4, **kwargs):
#     return a, args, kwargs, d, n, m, r
#
#
# print(func(5, 1, 7, 9, 8, 4, 6, b=2, c=3, d=7))


# name = "Tom"  # глобальная
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"  # локальная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5
# x = 6
#
#
# def func(a):
#     # x = 2
#
#     def inner():
#         # x = 4
#         return a + x
#
#     return inner()
#
#
# print(func(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World!")

# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         # a = 4  # 5
#         print("Сумма:", a + b)
#
#     print("a =", a)  # 3
#     # a = 6
#     fun2(4)  # 4
#
#
# fun1()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 35 = 60
# print(c)
# x = 5
#
#
# def fn1():
#     x = 25  # 25
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2  # 1
#         b = b1 + b2  # 7
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# def outer(a, b, c):
#     def inner(x, y):
#         return x * y
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(20))

# print(outer(4)(6))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0  # 2
#
#     def inner():
#         nonlocal s
#         s += 1  # s = s + 1  => 3
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
#
# res1()
# res1()
# res1()
# res1()
# res1()
#
# res2()
# res2()
# res2()
# res2()
# res2()
#
#
# res3 = func("Сочи")
# res3()
# res3()
# res3()

# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def make(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# bal_A = make(80, 100)
# bal_B = make(70, 80)
# bal_C = make(50, 70)
# bal_D = make(0, 50)
# print(bal_A(students))
# print(bal_B(students))
# print(bal_C(students))
# print(bal_D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         return "Hello"
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# # print(obj1())
# print(obj1.add())  # сумма
# print(obj1.sub())  # разность
# print(obj1.mul())  # произведение


# Анонимные функции (lambda-выражения)


# def summa(x=5, y=7):
#     return x + y
#
#
# print(summa())
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 7, 8, 9))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(42)
# print(f1(1))
#
# outer2 = lambda n: lambda x: x + n
#
#
# f2 = outer2(42)
# print(f2(1))
#
# print((lambda n: lambda x: x + n)(42)(1))
#
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# def sort_val(i):
#     return i[1]
#
#
# d = {'c': 10, 'a': 15, 'b': 4}
# q = list(d.items())
# print(q)
# # q.sort(key=lambda i: i[1], reverse=True)
# q.sort(key=sort_val, reverse=True)
# print(q)
# d1 = dict(q)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[2]()
# print(d[2])

# map(func, iter), filter(func, iter)

# def mult(t):
#     return t * 2


# lst = [2, 8, 12, 5, 10]

# a = list(map(mult, lst))
# a = list(map(lambda t: t * 2, lst))
# a = set(map(lambda t: t * 2, [2, 8, 12, 5, 10]))
# print(a)


# t = (2.88, -1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
# t3 = tuple(map(int, t))
# print(t3)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)

# filter(func, iter)

# t = ('abcd', 'abc', 'cdert', 'def', 'gfi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: (s > 75) and s < 80, b))
# print(res)

# Декоратор
# def hello():
#     return 'Hello "hello"'
#
#
# def super_func(func):
#     print('Hello "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello "hello"'
#
#
# print(id(hello))
# test = hello
# print(id(test))
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('*' * 20)
#         func()
#         print('=' * 20)
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello 'func_test'")
#
#
# @my_decorator
# def hello():
#     print('Hello "hello"')
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     c = 0
#
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print("Вызов функции:", c)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Резникова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg):  # 3
#     def outer(func):  # return_num
#         def wrap(*args, **kwargs):  # num
#             return arg * func(*args, **kwargs)
#
#         return wrap
#
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# @multiply(3)
# def mul(*num, c=1):
#     return sum(num) / c
#
#
# print(return_num(5))
# print(mul(5, 5, 9, 7, 8, 3, c=2))
# print(mul(1, 8, 7, 6, 4, 2, 8, 7, 4, 9, 2))

# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Неверный тип данных")
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Неверный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return outer
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "!"))
#
# print(typed_fn2("Hello", "world", "!"))
# # print(typed_fn2(6, 4, 2))
#
# print(typed_fn3("Hello", "world", z='5'))

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("t" in e)
# print(e[::-1])

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
#
# print(r"C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt" + "\\")
# print("C:\\folder\\file.txt\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# print(f"Число: {round(10 / 3, 2)}")
# print(f"Число: {10 / 3:.2f}")

# x = 10
# y = 5
# # print(f"{x = }, {y = }")
# # print("x=", x, sep="")
# print(x, "x", y, "/", 2, "=", x * y / 2)  # 10 x 5 / 2 = 25.0
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
# print(F"{{{{{num}}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print(r'home' + "\\" + dir_name + "\\" + file_name)
# print(f'home\\{dir_name}\\{file_name}')

# 'Hello world gfghftghf dfgfghdfghdfghdfgh'
#
# """Hello    !!!!
#             world
# dfvdsdxf
# sdsdfdsf
# sdfdsfdsf
# """
#
# s1 = '''Hello
#             world'''
#
# # print(s)
# print(s1)
# # print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print()
# print(len.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('A'))
# print(ord('А'))
# print(ord('й'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "Test string for met"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(1055))

# a = 97
# b = 122
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# print("apple" > "Apple")  # 97 > 65
# print(ord('a'))
# print(ord('A'))

# from random import randint
#
# SHORTEST = 8
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         # print(rand_char)
#         res += rand_char  # res = res + rand_char
#
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python!"
# print(s.capitalize())  # Hello, world! i am learning python!
# print(s.lower())  # hello, world! i am learning python!
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON!
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON!
# print(s.title())  # Hello, World! I Am Learning Python!

# print(s.count("h", 1, -4))  # кол-во заданных элементов
# print(s.find("Py", 0, 30))  # возвращает индекс заданного элемента или "-1" - если элемента нет
# print(s.rfind("h"))  # поиск с конца

# print(s.index("h"))  # возвращает индекс заданного элемента или ValueError - если элемента нет
# print(s.rindex("h"))  # поиск с конца

# s1 = "I am learning Python. hello, WORLD!"
# s1 = s1[:s1.find('h')] + s1[s1.rfind('h') + 1:]
# print(s1)
# print(s.find("I am"))
# print(s.startswith("I am", 14))  # поиск заданной подстроки с начала, возвращает значение bool
# print(s.endswith("Python"))  # поиск заданной подстроки с конца, возвращает значение bool

# print('123asd'.isalnum())  # состоит ли строка из букв или цифр
# print('ASDnmj'.isalpha())  # состоит ли строка из букв
# print('1230'.isdigit())  # состоит ли строка из цифр
# print('abc#$%123'.islower())  # проверка только букв на нижний регистр
# print("ASD4534;%%q".isupper())  # проверка только букв на верхний регистр


# print('py'.center(10, "-"))

# def avg(fn):
#     def wrap(*args):
#         # a = ""
#         # for i in args:
#         #     a += str(i) + ", "
#         # print(args)  # (2, 3, 3, 4)
#         a = ", ".join(map(str, args))  # ('2', '3', '3', '4')
#         print("Среднее арифметическое:", a, "=", fn(*args) / len(args))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     a = ""
#     for i in args:
#         a += str(i) + ", "  # 2, 3, 3, 4,
#     print("Сумма чисел:", a[:-2], "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)

# удаляют пробельные символы в строке
# print("       py".lstrip())
# print("py        ".rstrip())
# print("          py        ".strip())

# print('https://www.python.org'.lstrip('/:pths'))
# print('https://www.python/.org'.lstrip('/:pths').rstrip("org."))
# print('https://www.python/.org'.strip('/:pthsorg.'))

# s = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(s.replace('Nython', 'Python', 2))  # поиск и замена

# преобразует итерируемый объект в строку
# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("...".join(['1', '99']))
#
# print(":".join("Hello"))

# print('Строка разделенная пробелами'.split())  # разбивает строку на список подстрок
# print('www.python.org.ru'.split(".", 1))
# print('www.python.org.ru'.rsplit(".", 1))

# a = input("Введите ФИО: ").split()
# print(a)
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')

# Регулярные выражения

# import re
# from re import split

# s = "Я ищу совпадения в 2023 году. [^] И я их найду в 2 счёта. 478_9-6. Hello World 200000000000000000000"
# reg = r'\d'  # [3-5]
# reg = r'\w'
# reg = r'\s'
# reg = r'\S'
# reg = r'\W'
# reg = r'\D'
# reg = r'\d+'
# reg = r'20*'
# # reg = r'[203]'
# # reg = r'[12][0-9][0-9][0-9]'
# # reg = r'[А-ЯЁа-яё]'
# # reg = r'[А-яЁё]'
# # reg = r'[a-zA-Z]'
# # reg = r'[\[^\].]'
# reg = r'[^0-9]'
# # reg = r'[A-z]'
# # print(re.findall(reg, s))  # возвращает список, содержащий все совпадения или []
# # print(re.search(reg, s))  # возвращает перовое совпадение с искомым шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# # print(re.match(reg, s))  # возвращает перовое совпадение с искомым шаблоном только вначале строки
#
# # print(re.split(reg, s, 5))  # разбивает строку на список подстрок по заданному шаблону
# # print(re.sub(reg, "!", s))  # поиск и замена
# print(re.findall(reg, s))
# print(ord("А"))
# print(ord("Я"))
# print(ord("а"))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T18:00. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# print(re.findall(reg, s))

# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# # print(re.findall(r'[+-]?\d+\.?\d*', d))
# print(re.findall(r'[+-]?[\d.]+', d))

# print("Hello git!!!")
#
# print("Hello GitHub!!!")

# print("Строка, созданная в новом репозитории")

import re

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('#.*', '', s))
# # Дата рождения: 05.03.1987
# print("Дата рождения:", re.sub("-", ".", re.sub('#.*', '', s)))

# s = "12 сентября 2023 год 4567891"
# req = r'\d{,4}'
# print(re.findall(req, s))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'^\w+\s\w+'
# # reg = r'^\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pytgdfgdfgdfg"))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w\+", text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall('one$', text))
# print(re.findall('one$', text, flags=re.MULTILINE))


# print(re.findall("""[a-z.-]+@[a-z.-]+""", 'test@mail.ru'))
# print(re.findall("""
# [a-z.-]+   # part 1
# @          # @
# [a-z.-]+   # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# s = "12 сентября 2023 год 4567891"
# req = r'\d{2,4}?'
# print(re.findall(req, s))

# s = "<p>Изображение <img  alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Николай"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f, int"
# # reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# reg = r"((int|double)\s*=\s*(\d+[.\w+]*))"
# print(re.findall(reg, s))

# s = '127.0.0.1'
# s = '192.168.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'(([a-z]+)(\d+))'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))
#
# s1 = "5 + 7*2 - 4"
# reg1 = r'\s*([+*-])\s*'
# print(re.split(reg1, s1))

# 1900 - 2099
# a = "31-10-1978"
# req = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(req, a))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'(\d+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", repl_find, text))

# s = "<p>Изображение <img  alt='картинка' src=\'bg.jpg\'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'  # (?P<name>...) (?P=name)
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))  # 23.10.2023

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))

# Файлы

# f = open('D:/Python327/test.txt')
# f = open('test.txt')
# print(f)
# print(*f)

#
# f = open('test.txt', 'r')
# print(f.read(3))
# f.close()
#
# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# print(f.readline())  # '\n'
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('text.txt', 'r')
# print(f.readlines(14))
# print(f.readlines())
# f.close()

# f = open('text.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open('text.txt', 'r')
# for line in f:
#     count += 1
# f.close()
# print(count)

# f = open('text.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()

# f = open('xyz.txt', 'a')
# # print(f.write('\nNew text.'))
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# print(f.writelines(lines))
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello World\n"
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('test.txt')
# print(f.read(3))
# print(f.tell())  # на какой позиции находится курсор
# print(f.seek(1))  # перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test4.txt', 'r+')
# print(f.write("I am learning Python"))  # 20
# print(f.seek(3))  # I a|m learning Python
# print(f.write("-new string-"))  # 12
# print(f.tell())  # 15
# f.close()


# with open('test.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('test.txt', 'r+') as f:
#     print(f.read())

# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = "res_1.txt"


# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))  # f.write('4.5 2.8 3.9 1.0 0.3 4.33 7.777')
# get_line(lst)
# print('Done!')

# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)  # str
#
# nums_list = list(map(float, nums.split()))  # list(map(float, ['4.5', '2.8', '3.9', '1.0', '0.3', '4.33', '7.777']))
# # num_list = nums.split()
# print(nums_list)
# # print(type(nums_list[0]))
# print(len(nums_list))


# def longest_words(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         # print(w)
#         max_length = len(max(w, key=len))
#         # print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         # print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('file.txt'))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)


# read_file = 'one.txt'
# write_file = 'two.txt'
# res = 'three.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(res, 'w') as res:
#     # f1 = fr.readlines()
#     # f2 = fw.readlines()
#     # print(f1)
#     # print(f2)
#     # f3 = f1 + f2
#     # res.writelines(f3)
#     for i, j in zip(fr, fw):
#         res.write(i[:-1] + " -> " + j)

# Модуль OS (OS.PATH)

# import os


# print("Текущая директория:", os.getcwd())  # путь к файлу
# print(os.listdir())  # список папок и файлов, находящихся в текущей директории
# print(os.listdir("E:"))  #

# os.mkdir("folder1")  # создать папку (без промежуточных путей)
# os.makedirs("nested1/nested2/nested3")  # может создавать вложенные папки

# os.remove('test.txt')  # удаляет файл

# os.remove('folder/file.txt')

# os.rmdir('folder1')  # удаляет папку (но только пустую)

# os.rename("xyz.txt", "first.txt")  # переименование и перемещение файла
# os.rename("first.txt", "nested1/first.txt")
# os.rename('folder', 'nested1/folder')


# for root, dirs, files in os.walk('nested1', topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в папке {root_tree}")
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
#     print('-' * 50)
#
#
# remove_empty_dirs('nested1')


import os.path


# print(os.path.split(r'D:\Python327\nested1\nested2\nested3\two.txt'))  # разбивает путь на кортежи (путь,
# # имя документа)
#
# print(os.path.exists(r'D:\Python327\nested1\nested2\nested3'))  # проверяет существование заданного пути
#
# print(os.path.join('nested1', r'D:\Python327', 'nested2', 'two.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\f21': ['f211.txt', 'f212.txt']
# }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\f21\f211.txt', r'Work\F2\f21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Какой-то текст для файла {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, file in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(file)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# import time
#
# path = "main.py"
# size = os.path.getsize(path)  # 'bytes'
# print(size // 1024, "KB")  # размер файла
# ctime = os.path.getctime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(ctime)))  # время создания файла в секундах
# print(os.path.getatime(path))  # время последнего доступа к файла в секундах
# print(os.path.getmtime(path))  # время последнего изменения файла в секундах


# file_path = 'nested1/nested2'

# if os.path.exists(file_path):
#     dir0, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({dir0}) - время последнего доступа к файлу:", atime, "сек")
# else:
#     print(f'Файл {file_path} не существует!')

# print(os.path.isfile(file_path))  # возвращает True, если путь является файлом
# print(os.path.isdir(file_path))  # возвращает True, если путь является папкой

# dir_name = 'nested1'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     print("p =>", p)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     else:
#         print(f"{obj} - dir")

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)   # 0
#     print(n, end=" ")
#
#
# n1 = int(input("На каком этаже Вы находитесь: "))
# elevator(n1)  # 5


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i  # res = res + i  # 25 = 16 + 9
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         return lst[0]  # 9 +
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25  # 1 + 3 + 5 + 7


# def to_str(n, base):  # (15, 16)
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # F
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 14 = E
#
#
# print(to_str(254, 16))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# print(names[3][0])

# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return remove(text[1:]) + text[0]  # HelloWorld
#
#
# print(remove("  Hello\tWorld!!!      "))


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
# p1.x = 10
# print(p1.x)
# print(type(p1))
#
# p2 = Point()
# print(p2.x)
#
# print(id(p1))
# print(id(p2))
# print(id(Point))
#
# p1.z = 5
# print(p1.z)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)
# print(Point.__doc__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p2 = Point()
# p1.set_coord(5, 10)
# # Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
# p2.set_coord(20, 70)
# # Point.set_coord(p2, 20, 70)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}"
#               f"\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.address = address
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#
#     def set_city(self, value):  # установить
#         self.city = value
#
#     def get_city(self):  # получить
#         return self.city
#
#     def set_name(self, value):
#         self.name = value
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_city("Владимир")
# print(h1.get_city())
# h1.set_name("Валентина")
# print(h1.get_name())


# import os
#
# root = r"files"
# obj = os.listdir(root)
# print(obj)
#
# lst = []
# for ob in obj:
#     p = os.path.join(root, ob)
#     lst.append(p)
#
# print(lst)
#
# # obj_sort = sorted(lst, key=os.path.isfile, reverse=True)
# # print(obj_sort)
#
# lst.sort(key=os.path.isfile, reverse=True)
# print(lst)

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):  # инициализатор
#         self.name = name
#         self.surname = surname
#         print("Инициализатор")
#
#     def __del__(self):  # деструктор
#         print("Деструктор")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k  # self.skill = self.skill + k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
# print()
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0  #
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1  # count = count + 1
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p2 = Point(2, 7)
# print(p2.get_coord())
# p3 = Point(10, 20)
# print(p3.get_coord())
# print(p3.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним.")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("R-5ST")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить
#         # if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
# # p1.set_coord(20.5, 50)
# print(p1.get_coord())
# p1.set_x("100")
# print(p1.__dict__)
# # print(Point.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)

# class Point:
#     # __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_x("100")
# p1.z = 5
# # print(p1.__dict__)
# print(p1.z)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def __get_x(self):
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = "100"
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property  # получение данных
#     def x(self):
#         return self.__x
#
#     @x.setter  # установка данных
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     @x.deleter  # удаление данных
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# # del p1.x
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__old
#
#     @age.setter
#     def age(self, value):
#         self.__old = value
#
#     @age.deleter
#     def age(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.age = 31
# print(p1.age)
# del p1.name
# del p1.age
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     # @staticmethod
#     # def max(a, b, c, d):
#     #     mx = a
#     #     if b > mx:
#     #         mx = b
#     #     if c > mx:
#     #         mx = c
#     #     if d > mx:
#     #         mx = d
#     #     return mx
#
#     @staticmethod
#     def max(*args):
#         res = args[0]
#         for i in args:
#             if i > res:
#                 res = i
#         return res
#
#     @staticmethod
#     def min(*args):
#         res = args[0]
#         for i in args:
#             if i < res:
#                 res = i
#         return res
#
#     # @staticmethod
#     # def average(*args):
#     #     return sum(args) / len(args)
#
#     # @staticmethod
#     # def average(*args):
#     #     res = 0
#     #     count = 0
#     #     for i in args:
#     #         res += i
#     #         count += 1
#     #     return res / count
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))
# 5! = 1*2*3*4*5


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day45, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day45, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # dt1 = Date.from_string("23.10.2023")
# # print(dt1.string_to_db())
# # dt2 = Date.from_string("21.12.2022")
# # print(dt2.string_to_db())
# dates = [
#     '30.12.2023',
#     '30-12-2023',
#     '01.01.2023',
#     '12.31.2023'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         dt1 = Date.from_string(string_date)
#         print(dt1.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным число от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# p1.old = 27
# print(p1.old)
# p1.password = "4567 123456"
# print(p1.password)
# p1.weight = 70.0
# print(p1.weight)
# print(p1.__dict__)


# Наследование

# class Point(object):
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# print(issubclass(Point, object))
# print(type(5))


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор базового класса")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args, **kwargs):
#         print("Переопределенный инициализатор класса Line")
#         # Prop.__init__(self, *args, **kwargs)
#         super().__init__(*args, **kwargs)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 2)
# line.draw_line()

# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# DRY (Don`t Repeat Yourself) - не повторяйся!


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")

property
def height(self):
    return self.__height

@height.setter
def height(self, h):
    if h > 0:
        self.__height = h
    else:
        raise ValueError("Ширина должна быть положительным числом")

def area(self):
    print(f"Площадь {self.color} прямоугольника:", end=" ")
    return self.__width * self.__height
        # return self.width * self.height


# rect = Rectangle(10, 20, "green")
# print(rect.color)
# print(rect.width)
# print(rect.height)
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(45, 90), Point(20, 95))
# rect.draw_rect()
# rect.set_coord(Point(10.5, 50), Point(45.8, 94.8))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


#  Перегрузка методов


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата должны быть целым числом")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координата должны быть целым числом")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()
# line.set_coord(ep=Point(50, 300))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figure = list()
# figure.append(Line(Point(0, 0), Point(10, 10)))
# figure.append(Line(Point(10, 10), Point(20, 10)))
# figure.append(Rect(Point(50, 50), Point(100, 100)))
# figure.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figure:
#     f.draw()

from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())

t2 = SqTable(20)
print(t2.__dict__)
# print(t2.calc_area())

t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())

