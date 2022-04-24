from sys import argv
from os.path import exists
script,file_name=argv
if(exists(file_name)):
	print "File name already exists... overwriting with the input"

text=raw_input("Say something...")
print "You said%r" %text
f=open(file_name,"w+")
f.truncate()
f.write(text)
#f.close()

#f=open(file_name)
print f.read()
f.close()

