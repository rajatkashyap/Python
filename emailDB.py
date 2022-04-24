import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname=raw_input('Enter file name:')
fh=open(fname)
for line in fh:
	if not line.startswith('From:'): continue
	pieces=line.split()
	email=pieces[1]
	#print email
	cur.execute('select count from Counts where email = ?',(email,))
	row=cur.fetchone()
	if row is None:
		cur.execute('Insert into Counts values (?,1)',(email,))
	else:
		cur.execute('update Counts set count=count+1 where email = ? ',(email,))
'''	try:
		row=cur.fetchone()[0]
		cur.execute('update Counts set count=count+1 where email = ? ',(email,))
	except:	
		cur.execute('Insert into Counts values (?,1)',(email,))
		'''
		
		
conn.commit()
for row in (cur.execute('select * from Counts')):
	print row[0],row[1]

cur.close()

