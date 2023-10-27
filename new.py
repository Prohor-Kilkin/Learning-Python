# import requests
# import json
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(response.text)
# todos = json.loads(response.text)
# # print(todos)
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
#
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_user = "and".join(users)
#
#
# def keep(todo):
#     is_complete = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open("data_json", "w") as file:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, file, indent=2)


# import csv
# with open("data1.csv", "r") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы:{', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]}")
#
#         count += 1
#     print(f"Всего строк в файле:{count}")
#
# from bs4 import BeautifulSoup
# f = open('index.html', encoding="UTF8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", id="whois")
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena")
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("https://www.wildberries.ru/catalog/0/search.aspx?search=кроссовки%20мужские").text
# html = BeautifulSoup(r, "lxml")
# print(html)

import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summ REAL,
#     # data BLOB)""")
#     cur.execute("DROP TABLE users")

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     data BLOB NOT NULL DEFAULT "+79090000000"
#     )""")
    