a = tuple(input("Ведите элементы кортежа без пробелов: "))
print(a)
b = []
for i in a:
	if i not in b:
		b.append(i)
		print("Количество", i, "=", a.count(i))
