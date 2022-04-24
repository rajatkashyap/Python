w=raw_input("Enter words")
w1=w.split()
w2=[]
for w in w1:
	if w not in w2:
		w2.append(w)
print ' '.join(w2)