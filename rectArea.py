#!/usr/bin/python3
class rectArea:
	def __init__(self,length, breadth):
		self.length = length
		self.breadth = breadth
		calcArea(self.length,self.breadth)
	
	def calcArea(length,breadth):
		return lambda:length*breadth
	
l = 20
b = 40
area = rectArea(l,b)
print(area)
