from random import randint

n = int(input("Введите кол-во элементов в списке: "))
random_numbers = []
i = 1
while i <= n:
	element = randint(1, 10)
	if element not in random_numbers:
		random_numbers.append(element)
		i += 1
print("Уникальные случайные числа: ", random_numbers)


w, h = 5, 4
matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
print(matrix)
for row in matrix:
	for x in row:
		print(x, end="\t")
	print()
