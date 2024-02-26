"""
             OOPS - Task
Task 1
Create a class Employee with name and salary attributes.
The salary must be calculated and should be initialized to zero.
Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You
can give no of hours to the method as an argument.
Now create a child class PartTimeEmployee by inheriting the Employee class, and by using method
overriding (create salary calculation method in this class also with the same name)
get the salary of part time employee by multiplying no of hours worked by 150.
Create 3 objects for each class.
Now implement '+' operator overloading and find the total salary expense for keeping those
employees by adding up the objects together.
Eg:
e1 = Employee(name="John")
e1.update_salary(hours=6)
e2 = Employee(name="Robin")
e2.update_salary(hours=8)
e3 = PartTimeEmployee(name="Jake")
e3.update_salary(hours=8)
# The below line should work.
total_expense = e1 + e2 + e3      """


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def calculate_salary(self, work_hours):
        self.salary = work_hours * 200


class PartTimeEmployee(Employee):
    def calculate_salary(self, work_hours):
        self.salary = work_hours * 150


e1_name = input("Enter the name of the first employee: ")
e1_hours = int(input("Enter the number of hours worked by " + e1_name + ": "))

e2_name = input("Enter the name of the second employee: ")
e2_hours = int(input("Enter the number of hours worked by " + e2_name + ": "))

e3_name = input("Enter the name of the third employee: ")
e3_hours = int(input("Enter the number of hours worked by " + e3_name + ": "))

e1 = Employee(name=e1_name)
e1.calculate_salary(work_hours=e1_hours)

e2 = Employee(name=e2_name)
e2.calculate_salary(work_hours=e2_hours)

e3 = PartTimeEmployee(name=e3_name)
e3.calculate_salary(work_hours=e3_hours)


total_salary = e1.salary + e2.salary + e3.salary
print("Total salary expense:", total_salary)


""" Task 2
Extend the above solution and find the average expense per employee.
The calculation must be dynamic, there should be no need for you to manually code each addition
operations. This can be done by keeping track of the objects being created – in a list (But don’t
manually append the objects to a list, this must happen when the objects are being created).    """


class Employee:
    employees = []

    def __init__(self, name):
        self.name = name
        self.salary = 0
        Employee.employees.append(self)

    def calculate_salary(self, hours):
        self.salary = hours * 200


class PartTimeEmployee(Employee):
    def calculate_salary(self, hours):
        self.salary = hours * 150


e1 = Employee(name="Abin")
e1.calculate_salary(hours=9)

e2 = Employee(name="David")
e2.calculate_salary(hours=8)

e3 = PartTimeEmployee(name="John")
e3.calculate_salary(hours=6)

total_expense = sum(e.salary for e in Employee.employees)

average_expense_per_employee = total_expense / len(Employee.employees)

print("Total salary expense:", total_expense)
print("Average expense per employee:", average_expense_per_employee)
