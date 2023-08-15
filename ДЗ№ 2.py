number = int(input("Введите пятизначное число: "))
first_digit = number % 10
number = number // 10
second_digit = number % 10
number = number // 10
third_digit = number % 10
number = number // 10
fourth_digit = number % 10
number = number // 10
fifth_digit = number % 10
composition = first_digit * second_digit * third_digit * fourth_digit * fifth_digit
average = (first_digit * second_digit * third_digit * fourth_digit * fifth_digit) / 5
print("Произведение всех цифр этого числа:  ", composition)
print("Среднее арифметическое: ", round(average, 2))







