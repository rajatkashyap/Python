file=raw_input('Enter file name:')
with open(file) as f:
	for line in f:
		print line
	print f.tell()
	f.seek(1)
	print f.tell()
	print f.read()
	f.seek(0)
	print f.readlines()
	f.seek(0)
	print f.readline()
	print f.readline()
	