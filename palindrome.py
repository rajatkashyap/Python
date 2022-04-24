input='artrartrt'
pal=[]
l=len(input)
for i in range(l):
	for j in range(i+1,l):
		sub=input[i:j]
		if sub==sub[::-1]:
			pal.append(sub)
		
print pal	
print max(pal,key=len)


input='Rajar'
input=input.lower()
palin=True
for i in range(len(input)):
	if input[i]!=input[len(input)-1-i]:
		palin=False
	
print "%s text is Palindrome?" %input, palin