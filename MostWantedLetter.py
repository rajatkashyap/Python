def checkio(text):
    a=[]
    b=[]
    text_low=text.lower()
    text1=text_low.replace(" ","")
    for i in text1:
        if i.isalpha():
            a.append(text1.count(i))
			
	print max(a)		
			
	for i in range(0,len(a)):
		if a[i]==max(a):
			b.append(text1[i])
	print b
    return min(b)
print checkio('Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!')
#print checkio('tfweuifukwe foeof RRR')