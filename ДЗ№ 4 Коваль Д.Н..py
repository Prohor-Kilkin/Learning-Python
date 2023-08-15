list_ = [int(input("->")) for i in range(int(input("к-во элементов списка: ")))]
summ = 0
quantity = 0
for i in list_:
	summ += i
	if i != 0:
		quantity += 1
result = summ / quantity
print("Среднее арифметическое: ", result)
