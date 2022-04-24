i=int(raw_input())
l=[]
for x in range(i):
    a=raw_input()
    b=float(raw_input())
    l.append([a,b])


#l1=[[input(),float(input())] for x in range(i)]
#print l1

scores = sorted({s[1] for s in l})
result = sorted(s[0] for s in l if s[1] == scores[1])
print '\n'.join(result)
#print result