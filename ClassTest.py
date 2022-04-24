class first:
	def __init__(self,i):
		self.i=i
	
	def printlist(self):
		for x in self.i:
			print x

f1=first([1,2,3,4,100,200])			
f1.printlist()