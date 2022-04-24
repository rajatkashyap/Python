dict_words={}
s=raw_input("Enter text")
s1=s.split()
print s
for word in s1:
	word=word.lower()
	if word in dict_words:
		dict_words[word]+=1
	else:
		dict_words[word]=1
for word in dict_words:
	if dict_words[word]==1:
		print word
	

str_lower=[]
for i in s1:
	str_lower.append(i.lower())

print [x for x in str_lower if str_lower.count(x)==1]	