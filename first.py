print "Hello Rajat"
#print "How are you doing?"
cars=3
space_in_cars=4 
 
print cars,space_in_cars

print "There are", cars, "cars, with" , space_in_cars, "person space each"

name='Rajat'
hair_color='Black'
hieght=69 #inches
weight=70

print "My Name is %s," % name,"I am %d inches tall" % hieght,"and my hair color is %s." % hair_color
print "If I add %d and %d then I will get %d" % (hieght, weight,hieght +  weight)


#print '%(name)s has %(weight)03d weight'


x="There are %d types of people." %10
binary='binary'
dont='dont'

print x

print "I said: %s" %x
print "Who knows %s and those who %s" %(binary ,dont)

print binary
print dont

print binary+dont

print "Is weight greater than %d?:" %weight,weight>70
is_valid=0
while not is_valid:
	print "Whats your name?"
	name=raw_input('-->')
	print "Height?"
	try:
		height=int(raw_input('-->'))
		is_valid=1
	except ValueError,e:
	    print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])

print(35 *'*')
print(35 *'-')
print "His name is %s and height is %d" %(name,height)
print(35 *'-')
print(35 *'*')

from sys import argv
#script,first,second=argv
#print script
#print first
#print second

sign='>'

script,file=argv
txt=open(file)
print txt.read()

print "want to open another? (Y/N)"
ans=raw_input(sign)
if ans=='Y':
	print "File name please"
	file2=raw_input()
	txt2=open(file2)
	print txt2.read()
elif ans=='N':
	print "No problem, see you again!"
else:
	print "Wrong input dude!"
	
	
print 10>20






