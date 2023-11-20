from jinja2 import Environment, FileSystemLoader


x = "Домашняя работа"
y = "Домашняя работа выполнена"
z = "DZ_Jinja"
cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Renault', 'price': 44300},
    {'model': 'Wolksvagen', 'price': 21300}
]

file_loader = FileSystemLoader('jinja')
env = Environment(loader=file_loader)
tm = env.get_template('body.html')
msg = tm.render(text=x, text1=y, title=z, cars=cars)
print(msg)