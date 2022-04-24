from sys import argv
from os.path import exists
script,from_file,to_file = argv
print "copying data from %r to %r" %(from_file,to_file)

f=open(from_file)
print f.read()
f.close()
print "Exists?%r" %exists(to_file)
print "Do you want to continue? Enter to continue, Ctrl+C to get the heck out"
raw_input()
f=open(from_file)
print f.read()
f.close()
f1=open(to_file,'w')
f1.truncate()
f=open(from_file)

print f.read()
f1.write(f.read())

f.close()
f1.close()
f2=open(to_file)
print f2.read()