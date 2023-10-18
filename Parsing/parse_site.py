

import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    data = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        apartments = self.html.find_all("div", class_="text_block")
        for item in apartments:
            title = item.find("a").text
            address = item.find("div", class_="address").text
            price = item.find("div", class_="price").text
            self.data.append({"Квартира": title,
                              "Адрес:": address,
                              "Цена:": price})

    def save(self):
        with open(self.path, "a", encoding="utf-8") as f:
            for item in self.data:
                for key in item:
                    f.write(f"{item[key]}\n")






