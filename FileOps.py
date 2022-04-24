file=raw_input('Enter file name:')

def rewind(f):
	f.seek(0)
	
with open(file) as f:
	for line in f:
		print line
	print f.tell()
	rewind(f)
	print f.tell()
	print f.read()
	rewind(f)
	print f.readlines()
	rewind(f)
	print f.readline()
	print f.tell()
	print f.readline()
