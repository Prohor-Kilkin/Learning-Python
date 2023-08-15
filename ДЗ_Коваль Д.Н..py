# -------------------------------Вариант с локальной переменной-----------------------------
def calc_square(a, b, c):
	def rectangle(n, w):
		return n * w

	s = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
	return s


print(calc_square(2, 4, 6))


# --------------------Вариант с глобальной переменной----------------------------
#
# s = 0
#
#
# def calc_square(a, b, c):
# 	def rectangle(n, w):
# 		return n * w
#
# 	global s
# 	s = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
#
#
# calc_square(5, 8, 2)
# print(s)

# ----------------------------Вариант с нелокальной переменной-------------------------


# def calc_square(a, b, c):
# 	s = 0
#
# 	def rectangle(x, y, z):
# 		nonlocal s
# 		s = 2 * ((x * z) + (x * y) + (y * z))
#
# 	rectangle(a, b, c)
#
# 	print(s)


calc_square(5, 8, 2)
