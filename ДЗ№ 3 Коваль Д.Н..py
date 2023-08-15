coin = int(input("Введите число от 1 до 99: "))
first_digit = coin // 10
second_digit = coin % 10
result = ""
if first_digit == 1 or second_digit >= 5 or second_digit == 0:
	result = "копеек"
elif 1 < second_digit <= 4:
	result = "копейки"
elif second_digit == 1:
	result = "копейка"
print(coin, result)
