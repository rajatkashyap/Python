from sys import argv
script,l,b=argv
def rect_area(len,bre):
	area=len * bre
	return area
	
l=int(l)
b=int(b)	
print rect_area(l,b)