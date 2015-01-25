class Animal:
	def __init__(self, name, age, color, size,):
		self.size = size
		self. age = age
		self.color = color
		self.name = name
	def get_all(self):
		print(str(self)+"size = " + self.size)
		print("age = " + str(self.age))
		print("color = " + self.color)
		print("name = " + self.name)
	def eat(self, food):
		print("The animal, " + self.name.capitalize() + ", is eating " + food + "!")
	def sleep(self, hours):
		print("The animal, " + self.name.capitalize() + ", will sleep for " + str(hours) + " hours.")
dog = Animal("coby", 3, "black", "big")
lion = Animal("guy", 1, "orange", "tiny")
lion.eat("babies")
dog.sleep(8)