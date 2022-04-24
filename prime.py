i=int(raw_input())
a=[]
'''for p in range(2,i+1):
    for j in range(2,p):
        if p%j==0:
            break
        else:

            a.append(p)

print list(set(a))'''


for i in range(2,i+1):
    for j in range(2,i):
         #if i==2:
         #   a.append(i)
        if i%j==0:
            break
    else:
        a.append(i)

print a

