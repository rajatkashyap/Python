class fruit(object):
	def __init__(self,name):
		self.name=name
	
#	def printN(self):
#		print self.name


class thing(fruit):
	def __init__(self,name,color):
		fruit.__init__(self,name)
		self.color=color
			
		
#apple=fruit('apple')
#apple.printN()
t1=thing('apple','red')
print t1.name
print t1.color
		
	
	
	