from sys import argv
file=raw_input('Filename?')
'''with open(file) as f:
	for line in f:
		print line
'''

for line in open(file):
	print line