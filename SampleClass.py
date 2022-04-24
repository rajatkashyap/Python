class sample(object):
	def __init__(self,l):
		self.l=l
	
	def printlist(self):
		for i in self.l:
			print i

s1=sample([1,2,3])
s1.printlist()