def my_decorator(func):
	def wrap(*args):
		x = func(*args) / len(args)
		print('Среднее арифметическое: ', x)

	return wrap


@my_decorator
def summ(*f_args):
	s = sum(f_args)
	print('Сумма всех чисел:  ', s)
	return s


summ(1, 2, 3)
