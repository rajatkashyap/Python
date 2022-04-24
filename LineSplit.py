import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()


fname=raw_input('Enter file name:')
fh=open(fname)
for line in fh:
	if not line.startswith('from:'): continue
	pieces=line.split()
	print('*' * 40)
	for i in range(len(pieces)):
		print pieces[i]
	print('*' * 40)
	print('*' * 40)
   	for i in pieces:
		print i
	 	