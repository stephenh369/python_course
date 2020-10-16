import csv

class Employee:

  def __init__(self, first_name, last_name, hourly_rate, hours_worked, amount_due):
    self.first_name = first_name
    self.last_name = last_name
    self.hourly_rate = float(hourly_rate)
    self.hours_worked = int(hours_worked)
    self.amount_due = float(amount_due)

  def values_as_list(self):
    return [self.first_name, self.last_name, self.hourly_rate, self.hours_worked, self.amount_due]

# with open("employees.csv", "a") as csvfile:
#   writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#   employee = Employee("Jenny", "Jones", 12.50, 40, 0)
#   writer.writerow(employee.values_as_list())


employees = []

with open("employees.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  next(reader)
  for row in reader:
    current_employee = Employee(*row)
    employees.append(current_employee)

with open("employees.csv", "w") as csvfile:
  writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
  employees
  writer.writerow(["first_name", "last_name", "hourly_rate", "hours_worked", "amount_due"])

  for employee in employees:
    employee.amount_due = employee.hours_worked * employee.hourly_rate
    writer.writerow(employee.values_as_list())
