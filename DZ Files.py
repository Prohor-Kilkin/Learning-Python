# f = open('dz_files.txt', 'w')
# f.writelines("This is line 1\nThis is line 2\nThis is line 3\n")
# f.close()
# n = int(input('Введите номер строки для удаления: '))
# f = open('dz_files.txt', 'r')
# read_file = f.readlines()
# del read_file[n-1]
# f.close()
# f = open('dz_files.txt', 'w')
# f.writelines(read_file)
# f.close()


f = open('dz_files.txt', 'r', encoding='utf-8')
read_file = f.readlines()
print(read_file)
f.close()



