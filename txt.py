from sys import argv
script,filename = argv
txt=open(filename)
print txt.read()
file_n=raw_input("Whats your filename? Say it!!")
file_n=open(file_n)
print "Better!!"
print "Here you go"
print file_n.read()
