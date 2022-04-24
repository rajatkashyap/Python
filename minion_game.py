def minion_game(string):
	string=string.upper()
	vows=[]
	cons=[]
	for i in string:
		if i in ['A','E','I','O','U']:
			vows.append(i)
		else:
			cons.append(i)
	print vows
	print cons
	
	
minion_game('Banana')	