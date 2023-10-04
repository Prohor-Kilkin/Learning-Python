from pay import salary, hourly, commission, payroll, employee


salary = salary.SalaryEmployee(1, 'Валерий Задорожный', 1500)
hourly = hourly.HourlyEmployee(2, 'Илья Кромин', 40, 15)
commission = commission.CommissionEmployee(3, 'Николай Хорольский', 1000, 250)
system = payroll.PayrollSystem()
system.calc([salary, hourly, commission])
