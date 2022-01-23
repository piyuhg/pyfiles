#!/usr/bin/pthon3
class Parrot:
	## set the atributte to lets say a Bird
	species = "Bird"
	def __init__(self, name = 0, age = 0):
		self.name = name
		self.age = age
	
	def sing(self, song):
		return "{} is singing {}".format(self.name, song)

	def dance(self):
		return "{} is dancing".format(self.name)

blu = Parrot("Blu", 7)
woo = Parrot("Woo", 4)
kew = Parrot()

print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))
print("Kew is a {}".format(kew.__class__.species))

print("{} is {} years old".format(blu.name,blu.age))
print(kew.sing("I am so happy"))
print(woo.dance())
