f=open('UHC.txt')
dict={}
words=f.read().split()
for word in words:
	word.lower()
	dict[word]=dict.get(word,0)+1
val=dict.values()
val.sort(reverse=True)
val= val[:10]
for d in dict:
	if dict[d] in val:
		print d

	