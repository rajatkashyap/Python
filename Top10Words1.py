f=open('UHC.txt')
words=f.read().split()
dict_words={}
for word in words:
	word=word.lower()
	dict_words[word]=dict_words.get(word,0)+1

list_val=dict_words.values()
list_key=dict_words.keys()

list_val.sort(reverse=True)
print list_val
for i in list_key:
	if dict_words[i] in list_val[:10]:
		print "Word %r came %d times" %(i,dict_words[i])
		
print '*' * 30
	
for x in range(10):
	for key in list_key:
		if dict_words[key]==list_val[x]:
			print "Word %r came %d times" %(key,list_val[x])
		