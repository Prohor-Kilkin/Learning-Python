import time


def calc_time(func):
	def inner(*args):
		start = time.perf_counter_ns()
		func(*args)
		end = time.perf_counter_ns()
		print("Время выполнения функции: ", end - start, "нс")

	return inner


@calc_time
def sqrt(x):
	x = x + 1
	print(x)


sqrt(5)
