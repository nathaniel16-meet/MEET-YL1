class Animal:
	def __init__(self, name, age, color, size,):
		self.size = size
		self. age = age
		self.color = color
		self.name = name
	def get_all(self):
		print("size = " + self.size)
		print("age = " + str(self.age))
		print("color = " + self.color)
		print("name = " + self.name)
dog = Animal("coby", 3, "black", "big")
dog.get_all()