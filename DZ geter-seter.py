
# ======Вариант программы с getter и setter и проверкой на типы данных===================
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def set_surname(self, value):
#         if isinstance(value, str):
#             self.surname = value
#         else:
#             raise TypeError("Фамилия должна быть строкой")
#
#     def set_num(self, value):
#         if isinstance(value, int):
#             self.num = value
#         else:
#             raise TypeError("Номер счета должен быть числом")
#
#     def set_percent(self, value):
#         if isinstance(value, (int, float)):
#             self.percent = value
#         else:
#             raise TypeError("Проценты должны быть целым или вещественным числом")
#
#     def set_value(self, value):
#         if isinstance(value, (int, float)):
#             self.value = value
#         else:
#             raise TypeError("Сумма должна быть целым или вещественным числом")
#
#     def get_surname(self):
#         return self.surname
#
#     def get_num(self):
#         return self.num
#
#     def get_percent(self):
#         return self.percent
#
#     def get_value(self):
#         return self.value
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.set_surname("Пупкин")
# acc.print_info()
# print()
# acc.set_value(2548)
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


#  ==========Вариант программы с getter и setter на основе декоратора @property  и проверкой на типы данных=============


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @property
#     def surname(self):
#         return self.surname
#
#     @surname.setter
#     def surname(self, value):
#         if isinstance(value, str):
#             self.surname = value
#         else:
#             raise TypeError("Фамилия должна быть строкой")
#
#     @property
#     def num(self):
#         return self.num
#
#     @num.setter
#     def num(self, value):
#         if isinstance(value, int):
#             self.num = value
#         else:
#             raise TypeError("Номер счета должен быть числом")
#
#     @property
#     def percent(self):
#         return self.percent
#
#     @percent.setter
#     def percent(self, value):
#         if isinstance(value, (int, float)):
#             self.percent = value
#         else:
#             raise TypeError("Номер счета должен быть числом")
#
#     @property
#     def value(self):
#         return self.value
#
#     @value.setter
#     def value(self, value):
#         if isinstance(value, (int, float)):
#             self.value = value
#         else:
#             raise TypeError("Сумма должна быть целым или вещественным числом")
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
#
# acc.surname("Васечкин")
# acc.print_info()
# print()
#
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()
