import salary


class CommissionEmployee(salary.SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия"""
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate(self):
        fixed = super().calculate()
        return fixed + self.commission


if __name__ == '__main__':
    s = CommissionEmployee(1, "qwerty", 50, 800)
    print(s.calculate())