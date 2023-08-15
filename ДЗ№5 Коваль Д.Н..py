nums = [int(input("Введите элемент: ")) for i in range(int(input("Введите к-во элементов: ")))]
print("Начальный список: ", nums)
result_list = []
max_elem = 0
for i in range(len(nums)):
	if nums[i] > 0:
		result_list.append(nums[i])
	if nums[i] > nums[i-1]:
		max_elem = nums[i]
print("Список из положительных элементов: ", result_list)
print("Наибольший элемент: ", max_elem)
