s = "I am learning Python. hello WORLD!"
first_h = s.find('h')
second_h = s.find('h', first_h + 1, len(s))
part = s[first_h:second_h]
print(s[:first_h] + part[::-1] + s[second_h:])

