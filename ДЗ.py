sales = {
	'Петя': {
		'С': 3653,
		'Ю': 2143,
		'В': 9870,
		'З': 5453
	},
	'Вася': {
		'С': 3653,
		'Ю': 2143,
		'В': 9870,
		'З': 5453
	},
	'Маша': {
		'С': 3653,
		'Ю': 2143,
		'В': 9870,
		'З': 5453
	},
	'Даша': {
		'С': 3653,
		'Ю': 2143,
		'В': 9870,
		'З': 5453
	},
}
for i in sales:
	print(i, ':')
	for j in sales[i]:
		print('\t', j, ':', sales[i][j])
a = input('Введите имя: ')
b = input('Введите регион: ')
for i in sales:
	for j in sales[i]:
		if i == a and j == b:
			print('Объем продаж: ', sales[i][j])
			n = input('Введите новое значение: ')
			sales[i][j] = n
			print(sales[i])
