from sys import argv
script,file=argv
res=raw_input("Enter to continue CTRL+C to Exit")
f=open(file)
print f.read()
f.close()
f=open(file,'a+')
txt=raw_input("say something")
f.write(txt)
f.close()
f=open(file)
print f.read()