class PrintName():
	name='Rajat'
	def prnt(self):
		print "Name is %s" %self.name
		
		
	def __init__(self):
		print 'This is the first one'
		self.name='Parag'
	
	
		
name1=PrintName()
name1.prnt()
print name1.name
