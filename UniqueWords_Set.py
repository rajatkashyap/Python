w=raw_input("Enter words")
w1=w.split()
w2=list(set(w1))
print ' '.join(w2)