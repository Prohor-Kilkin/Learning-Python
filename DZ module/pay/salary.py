import employee


class SalaryEmployee(employee.Employee):
    """Административные работники, имеют фиксированную зарплату"""
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary


# if __name__ == '__main__':
#     s = SalaryEmployee(1, "qwerty", 50)
#     print(s.calculate())
