#!/usr/bin/python3
class Employee:
	'Common base class for all employees'
	empCount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print("Total Employee %d" %Employee.empCount)
		
	def displayEmployee(self):
		print("Name: ",self.name,", Salary: ",self.salary)

emp1 = Employee("ABC",1000)
emp1.displayCount()
emp1.displayEmployee()
print(id(Employee.empCount))
emp2 = Employee("DEF",2000)
emp2.displayCount()
emp2.displayEmployee()
print(id(Employee.empCount))
print(Employee.empCount)
emp2.name="HIJ"
emp2.displayEmployee()
emp1.tax = 7000
print(emp1.tax)
del emp1.salary
print(emp1.__class__.__name__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__weakref__)
