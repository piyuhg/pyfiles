#!/usr/bin/python3
class Parent:
	parentAttr = 100
	def __init__(self):
		print("Caling Parent Constructor")

	def parentMethod(self):
		print("Calling Parent Method")

class Child(Parent):
	def __init__(self):
		print("Calling Child Constructor")
		super().__init__()

	def childMethod(self):
		print("Calling Child Method")
		super().parentMethod()

p = Parent()
c = Child()
c.parentMethod()
		
