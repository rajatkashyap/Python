class animal(object):
	pass

class dog(animal):
	def __init__(self,name):
		self.name=name

class person(object):
	def __init__(self,name):
		self.name=name

class employee(person):
	def __init__(self,name,salary):
		super(employee,self).__init__(name)
		self.salary=salary
		
'''class employee(person):
	def __init__(self,name,salary):
		person.__init__(self,name)
		self.salary=salary
'''
		
rover=dog("Rover")
print rover.name

rajat=person("Rajat")
parag=employee("Parag",200000)
print rajat.name
print parag.name
print parag.salary

