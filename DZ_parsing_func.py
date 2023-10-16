import requests
from bs4 import BeautifulSoup
import csv


# parse_data = []
# url = "https://www.ixbt.com/live/index/news/"
# r = requests.get(url).text
# soup = BeautifulSoup(r, "lxml")
# data = soup.find_all("div", class_="thumbnail")
# for element in data:
#     header = element.find("h3", class_="topic-title").text
#     time = element.find("li", class_="topic-info-date").text.strip()
#     category = element.find("li", class_="topic-info-blog").text
#     parse_data.append({"time": time, "category": category, "header": header})
#
# with open("parse_news.csv", "w") as f:
#     for i in parse_data:
#
#         f.write(f"{i['time']}: {i['category']} - {i['header']}\n")


def get_html(url):
    response = requests.get(url)
    return response.text


def write_csv(data):
    with open("parse_news.csv", "a") as f:
        write = csv.writer(f, delimiter=" ", lineterminator="\n")
        write.writerow((data['time'], ":", data['category'], "-", data['header']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", class_="thumbnail")
    for element in data:
        header = element.find("h3", class_="topic-title").text
        time = element.find("li", class_="topic-info-date").text.strip()
        category = element.find("li", class_="topic-info-blog").text
        parse_data = {"time": time, "category": category, "header": header}
        write_csv(parse_data)


def main():
    url = "https://www.ixbt.com/live/index/news/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
