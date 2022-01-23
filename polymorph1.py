#!/usr/bin/python3
class Parrot:
	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot can't swim")

class Penguin:
	def fly(self):
		print("Penguin can't fly")
	
	def swim(self):
		print("Penguin can swim")

## below is a decorator
def flying_test(bird):
	bird.fly()

woo = Parrot()
pingu = Penguin()
flying_test(woo)
flying_test(pingu)
