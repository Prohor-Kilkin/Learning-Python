def my_decorator(func):
	def wrap():
		func()
		x = b / len(a)
		print('Среднее арифметическое: ', x)

	return wrap


@my_decorator
def summ():
	global a, b
	res = []
	a = input('Введите любые числа через пробел: ').split()
	for i in a:
		res.append(int(i))
		b = sum(res)
	print('Сумма всех чисел:  ', b)


summ()
