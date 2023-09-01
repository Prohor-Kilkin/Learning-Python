class Auto:
    model = ""
    production_year = ""
    producer = ""
    engine_power = ""
    color = ""
    price = ""

    def input_info(self, model, production_year, producer, engine_power, color, price):
        self.model = model
        self.production_year = production_year
        self.producer = producer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def print_info(self):
        print("*" * 10, "Данные об автомобиле", "*" * 10)
        print(f"Модель: {self.model}\nГод выпуска: {self.production_year}\nПроизводитель: {self.producer}\n"
              f"Мощность: {self.engine_power}\nЦвет: {self.color}\nЦена: {self.price}")
        print("=" * 42)

    def set_model(self, value):
        self.model = value

    def set_production_year(self, value):
        self.production_year = value

    def set_producer(self, value):
        self.producer = value

    def set_engine_power(self, value):
        self.engine_power = value

    def set_color(self, value):
        self.color = value

    def set_price(self, value):
        self.price = value

    def get_model(self):
        return self.model

    def get_production_year(self):
        return self.production_year

    def get_producer(self):
        return self.producer

    def get_engine_power(self):
        return self.engine_power

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


h1 = Auto()
h1.input_info("x7 M50i", "2021", "BMW", "530 л.с.", "черный", "10790000")
h1.print_info()
h1.set_color("белый")
h1.print_info()
print("Цена автомобиля: ", h1.get_price())