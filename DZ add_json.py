import json
import random


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += random.choice(letters)

    while len(tel) != 10:
        tel += random.choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data.update({random.randrange(0, 10**6): person_dict})
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())