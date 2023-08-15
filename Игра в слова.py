import time

main_word = input("Введите главное слово: ")
how_long = int(input("Время в секундах: "))
end_game = time.time() + how_long
s = []
res = 0
temp = []


def game(word):
	global res, temp
	for letter in word:
		while letter in main_word:
			s.append(letter)
			temp = "".join(s)
			break
	if temp == word:
		res += 1
		s.clear()
	else:
		print("Неверный ввод")
		s.clear()

		return res


while time.time() < end_game:
	game(input("Введите слово: "))
else:
	print(f"Количество придуманных слов: {res} шт")

