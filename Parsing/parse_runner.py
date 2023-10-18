from parse_site import Parser


def main():
    for i in range(1, 4):
        pars = Parser(f"https://www.moyareklama.ru/Смоленск/квартиры_продажа/все/8/{i}/", "apartments.txt")
        pars.run()


if __name__ == '__main__':
    main()
