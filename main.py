# name = 'DIMA'
# print("Hello,", name)
# age = 20
# print(age)
# print(name + age)
# a = 5
# print(a)
# print(id(a))
# print(type(a))
# a = 'hello'
# print(a)
# print(id(a))
# print(type(a))

# a = b = c = 1
# print(a,b,c)

# a, b, c, = 'hello', 5, 9.2
# print(a, b, c)
#
# PI = 3.14
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a = c
# a = b
# b = c

# print('строка \n символов 120 символов')
# print("D:\ folder\file")

# s1 = 'hello'
# s2 = 'World___'
# print(s1 + " " + s2)
# print(s2 * 3)
# print(6544884848484)
# print(6.544884848484)
# print(6+2)
# print(6 // 4)
# print(6 % 4)
# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("сумма:", res)
# print("произведение:", a * b * c)
# print("среднее:", res / 3)
# num = 4321
# print(num)
# res = num % 10 * 1000
# num = num // 10
# res += num // 10 * 100
# num = num // 10
# res += num // 10 * 10
# num = num // 10
# res += num // 10
# print(res)

# ===================15.06.=Ветвления==============================================

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# res1 = num1 + str(num2)
#
# print(res)
# print(res1)
#
# print(int(3.6846))
# a = 3.5145415
# a = round(a, 3)
# print(a)
# print(type(a))

# name = 'Dima'
# age = 37
# print('меня зовут', name, 'мне', age, 'лет' )

#
# a = int(input("Введите а: "))
# b = int(input("Введите b: "))
# c = int(input("Введите c: "))
# d = int(input("Введите d: "))

# True not true

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)


# False = "", 0, None

# print(  is None)

# && -and
# || - or
# ! - not

# -----------------------------------------------------------------------------
# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("Введите возраст"))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# day = int(input("Введите день недели цифрами"))
# if (day >= 1) and day <= 5:   # 1 <= day <= 5
#     print("Рабочий день")
# elif day == 6 or day == 7:
#     print("Выходной  день")
# else:
#     print("Такого дня не существует")


# ______________________20.06__Обработка исключений ,Циклы__________________
# n = int(input("Введите количество ворон(0-9): " ))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")


# тернарное выражение

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 40
# print("a ==  b" if a == b else "a > b" if a > b else "b > a")

# try:
#     n = int(input("Введите целое число:  "))
#     print(n * 2)
# except ValueError:
#     print("что-то не так")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально, вы ввели числа", n)
# finally:  # выводится в любом случае
#     print("конец программы")


# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1
#
# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


# a = int(input("Ведите число:  "))
# i = 0
# while i < a:
#     print("*",  end=" ")
#     i += 1
#
# print("*" * a)
#
# n = input("Введите целое число")
# while type(n) != int:
#     try:
#         n = int(n)
#     except  ValueError:
#         print("Число не целое")
#         n = input("Введите целое число")
#
#
#     if n % 2 == 0:
#         print('четное')
#     else:
#         print("нечетное")


# while True:
#  n = int(input(""))


#  ===================22/06===================
# вложенный цикл
# i = 1
# while i < 5:
#     print("внешний цикл: i=",  i)
#     j = 1
#     while j < 4:
#         print("\t внутренний цикл: J=",  j)
#         j += 1
#     i += 1

# таблица умножения

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*",  j, end="\t\t")
#     j += 1
# print(""*'')
# i += 1

# -------------------------------------------------------------------------------------------------

# for i in "hello":
#      print(i)
#
#
# for color in 'red', 'blue':
#      print(color)
#
#  for i in range(1, 15, 2): # (start, stop, step)
#      print(i)
#
#
# for i in range(3):
#     print(i)
#
# else:
#     print("Done!")

# a = [letter * 2 for letter in "hello"]
# print(a)

#  ============Списки================

#  nums = [15, 9, 3, 5, 8, "hello", 2.5]
# print(nums)
# print(nums[5])
# print(nums[-1])
# nums[5] = "HELLO WORLD"
# print(nums[5])
#
#
# print(len(nums))


# s = []
# print(s)
#
# b = list()
# print(b)

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [i**2 for i in range(1, n + 1)]  # генератор списков
# print(a)
#

# a = [i*3 for i in 'list']
# print(a)


# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# a =[0] * int(input("к-во элементов: "))
# for i in range(len(a)):
# 	a[i] = int(input("->"))
# 	print(a)

# a = [int(input("->")) for i in range(int(input("к-во элементов:")))]
# print(a)

# a = ['one', 'two', 'three']
# for i in range(len(a)):
# 	print(a[i], end=" ")
# print()
#
#
# for el in a:
# 	print(el, end=" ")

# n = list(range(21, 41))
# num = 0
# for i in n:
# 	if i % 2 == 0:
# 		num += 1
# print(num)


#  ======================27.06==============================


#  ----------МОДУЛИ--------------------

#  mport math
#
# num1 = math.sqrt(4)
# print(num1)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)

#  import math as m # псевдоним

# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)

# from math import ceil, floor  # (ctrl + left click)

#  ----------------------------------------------------

# import time

# sec = time.time()
# print(sec)
# local = time.ctime(87883568)
# print(local)
# res = time.localtime()
# print(res)
# print(res.tm_year)


# import locale  # региональные настройки

# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.str time("today is %B %d,%Y", time.localtime(235454)))

# print("start")
# time.sleep(5)
# print("program stopped")


# start = time.time()
# time.sleep(5)
# finish = time.time()
# print("process time", finish - start)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("process time", finish - start)


#  ------------------Срезы списков--[start:stop:step]


# s = [1, 2, 4, 5, 8]
# print(s[0:1])
# print(s[2:])
# print(s[:3])
# print(s[:])
# print(s[::-1])
# print(s[0:5:2])
# print(s[4:0:-1])
#
# # добавление в срез
#
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[3:5] = []
# del s[:]
# del s[:]
# print(s)

# ----------------МЕТОДЫ СПИСКОВ---------------

# s = [1, 2, 4, 5, 6, 7]
# print(s)
# s.append(99) # добавляет элемент в конец списка
# print(s)
# s.extend([8, 9, 10])
# print(s)
# s.extend("add")  # добавляет итерируемый объект
# print(s)
# s.insert(5, 10)  # добавляет элемент в заданное место
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
# 	x = int(input("Введите число: "))
# 	s.insert(0, x)
# print(s)

# a = [1, 2, 5, 4, 5, 8]
# b = [5, 4, 7, 2, 6]
# c = []
# for i in a:
# 	for j in b:
# 		if i in c:
# 			continue
# 		if i == j:
# 			c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 44]
# c = []
# if len(b) > len(a):
# 	for i in range(len(a)):
# 		c.append(a[i])
# 		c.append(b[i])
# for i in range(len(a), len(b)):
# c.append(b[i])
# else:
# for i in range(len(a)):
# 	c.append(a[i])
# 	c.append(b[i])
# for i in range(len(b), len(a)):
# c.append(b[i])
# print(c)

# s = [4, 2, 5, 6]
# s.remove(2)  # удаляет первый найденный элемент по заданному значению
# print(s)
#
# last = s.pop()  # удаляет и возвращает последний элемент
# print(last)
#
# last = s.pop(0)  # удаляет и возвращает элемент по заданному индексу
# print(last)
#
# s.clear()  # очищает список
# print(s)
#
# num = s.count(2)  # считает количество заданных элементов в списке
# print(num)
#
# ind = s.index(2)  # возвращает индекс первого найденного элемента по его значению
# print(ind)


#  =====================================29.06=================================

# a = [1, 2, 3]
# b = a
# print(a)
# print(b)
# a.append(28)
# print(a)
# print(b)
# b.append(38)
# print(a, id(a))
# print(b,  id(b))

#
# a = [1, 2, 3]
# b = a.copy()
# print(a)
# print(b)
# a.append(28)
# print(a)
# print(b)
# b.append(38)
# print(a, id(a))
# print(b, id(b))

# a = [1, 2, 3]
# a.reverse()  # перестраивает элементы списка задом на перед
# print(a)

# s = [2, 9, 8, 7, 2, 5]
# s.sort(reverse=True)  # сортировка по возрастанию и убыванию
# print(s)
# s.sort(key=len, reverse=True)

# s = [2, 9, 8, 7, 2, 5]
# s.sort()
# print(s)
#
# s1 = [2, 9, 8, 7, 2, 5]
# s.sorted


#  ____________Генерация случайных чисел-----------

#  from random import randint


#
# print(random())
# print(randint(5, 9))
# print(randrange(2, 9, 2))
# print(uniform(10.5, 25.5))
#
# city = ['moscow', 'smolensk', 'piter']
# print(choice(city))
# print(choices(city, k=2))
#
# a = [randint(0, 200) for i in range(int(10))]
# print(a)
#
# lst = [5, 2, 1, 4, 7, 8]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# x = list('2f8e5f7d')
# print(x)
# print('e' in x)
# print('a' not in x)
#
# lst = []
# if not lst:
# 	print("Список пуст")  # проверка на пустой список
#
# m = [
# 	[1, 2, 3, 4],
# 	[5, 6, 7, 8],
# 	[9, 10, 11, 12]
# ]
# print(m)
# print(m[1][2])
#
# for row in range(len(m)):
# 	print(m[row])
# 	for col in range(len(m[row])):
# 		print(m[row][col], end="\t\t")
# 	print()
#
# for row in m:
# 	for x in row:
# 		print(x, end="\t\t")
# 	print()
#
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
# 	print(x, '+', y, '=', x + y)

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]  # Генератор двумерных списков
# print(matrix)
# for row in matrix:
# 	for x in row:
# 		print(x, end="\t")
# 	print()


#  ==============================  4.07   ФУНКЦИИ  ==============================

#
# def hello(name):  # аргументы
# 	print("hello", name)
#
#
# hello("Dima")  # параметры
#
#
# def get_sum(a, b):
# 	print(a + b)
#
#
# c = 2
# d = 3
# get_sum(c, d)


# def symbol(count, a, b):
# 	for i in range(count):
# 		if i % 2 == 0:
# 			print(a, end="")
# 		else:
# 			print(b, end="")
#
# 	print()
#
#
# symbol(9, "+", "-")

#
# def get_sum(a, b):
# 	return a + b
#
#
# c = 2
# d = 3
# get_sum(c, d)
# res = get_sum(c, d)
# print(res)


# def cube(a):
# 	return a * a * a
#
#
# for i in range(1, 11):
# 	print(i, "в кубе = ", cube(i))


# def change(lst):
# 	lst[0], lst[-1] = lst[-1], lst[0]
# 	return lst
#
#
# print(change([1, 2, 3, 4, 5]))


# def func(x, y):
# 	if x > y:
# 		return True
# 	else:
# 		return False
#
#
# print(func(10, 5))
# print(func(5, 10))


# def check_password(password):  # _______Проверка надежности пароля_____________
# 	has_upper = False
# 	has_lower = False
# 	has_num = False
# 	for ch in password:
# 		if "A" <= ch <= "Z":
# 			has_upper = True
# 		elif "a" <= ch <= "z":
# 			has_lower = True
# 		elif "0" <= ch <= "9":
# 			has_num = True
# 	if len(password) >= 8 and has_upper and has_lower and has_num:
# 		return True
# 	return False
#
#
# p = input("enter password: ")
# if check_password(p):
# 	print("GOOD")
# else:
# 	print("bad")


# def get_sum(a, b, c, d=2):
# 	return a + b + c + d
#
#
# n = 2
# print(get_sum(1, 5, c=2, d=n))


#  +++++++++++++++++++++++++++  6.07  Кортеж   ++++++++++++++++++++++++++++++++++

# from random import randint

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# s = tuple([input("=>") for i in range(5)])
# print(s)

# s = tuple([randint(0, 10) for i in range(5)])
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(t3.count('a'))
# ch = 'a'
# if ch in t3:
# 	print(t3.index(ch))
# else:
# 	print('Такого символа нет')
#
#
# print(t3.index('l', 4))

# def slicer(tpl, el):
# 	if el in tpl:
# 		if tpl.count(el) > 1:
# 			first = tpl.index(el)
# 			second = tpl.index(el, first + 1)
# 			return tpl[first:second + 1]
# 		else:
# 			return tpl[tpl.index(el):]
# 	else:
# 		return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], ['hello'])
# print(t, id(t))
# t[3][0] = "new"
# print(t, id(t))
#
# t[3].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# x, y, z = t                                  #    Распаковка кортежей
# print(x, y, z)


# def get_user():
# 	name = "Dima"
# 	age = 37
# 	is_married = True
# 	return name, age, is_married
#
#
# # user = get_user()
# # n, year, married = user
#
#
# n, year, married = get_user()
# print(n, year, married)

# countries = (
# 	("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718)))
# )
#
# for country in countries:
# 	country_name, country_population, cities = country
# 	print("\nСтрана: ", country_name, "Население: ", country_population, cities, sep="")
# 	for city in cities:
# 		city_name, city_population = city
# 		print("\tГород", city_name,city_population)


# _____________________________МНОЖЕСТВО (SET)____________________________________

# s = {"banana", "apple", "orange"}
# print(s)
# for i in s:
# 	print(i)

# ----------------------------------------  11.07.Словари--------------------------------
# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2}
# print(type(d))
# print(d)
#
# d1 = dict(one=1, two=2)
# print(d1)

# users = [['a','b'],['c','d']]
# d_users = dict(users)
# print(d_users)

# d = {i: input("->")for i in range(1, 5)}       # Генератор словарей
# # print(d)
# # s = int(input("Delete element: "))
# # del d[s]
# # print(d)
# print(len(d))
#
# goods = {
# 	1: ['core i5', 9, 4500],
# 	2: ['core i3', 6, 3800],
# 	3: ['core i8', 6, 3600],
# 	4: ['core i6', 6, 4800],
# 	5: ['core i4', 6, 3900],
# }
#
# for i in goods:
# 	print(i, ") ", goods[i][0] ,"-", goods[i][1], "шт. по " , goods[i][2], sep="")
# while True:
# 	n = int(input("№:" ))
# 	if n !=0:
# 		k = int(input("Количество: "))
# 		goods[n][1] = k
# 	else:
# 		break


# +++++++++++++++++++++++++++++++++++++++   13.07  Функция zip  Области видимости +++++++++++++++++++++++++++++++++++++++++++++++++

# d = zip([1, 2, 3, ], ['one', 'two', 'three'])
# print(d)
#
# d = dict(zip([1, 2, 3, ], ['one', 'two', 'three']))
# print(d)
#
# d = list(zip([1, 2, 3, ], ['one', 'two', 'three']))
# print(d)
#
# a = []


#  =================================== 18.07  Замыкания =================================
#
# def outer(n):
# 	def inner(x):
# 		return n +x
#
# 	return inner
#
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(23))
#
# print(outer(4)(6))

# def func1():
# 	a = 1
# 	b = 'line'
# 	c = [1, 2, 3]
#
# 	def func2():
# 		return a, b, c
#
# 	return func2
#
#
# func = func1()
# print(func())

# ======================== Анонимные функции или Лямбда выражения ===================

# (lambda x, y: x + y)(1, 2)
# print((lambda x, y: x + y)(1, 2))

# a = (lambda x, y: x + y)
# print(a(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 8, 2, 5))


# print((lambda n: lambda x: x + n)(42)(5))                   #  Замыкание лямбда функций


# =================================20.07  Декораторы =======================

# def hello():
# 	return ""

# ==================================25.07=
#
# s = """hello
# world"""
# print(s)

# ===================================27.07========================

# print("  py".lstrip()) # убирает пробел слева
# print("py   ".rstrip()) # Убирает пробел справа
# print("  py   ".strip()) # Убирает пробелы с двух сторон
# print("https://www.python.org".lstrip("/spth:"))

# ======================15.08=========================

print('hello')
print('hello git')
