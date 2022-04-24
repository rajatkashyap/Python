i=int(raw_input())
dict={}
l=[]
for x in range(i):
    a=raw_input().split()
    l.append(a)
dict={l}
print dict
name=raw_input()
final=[]
for x in range(i):
        if name==l[x][0]:
            final=l[x]

avg= (float(final[1])+float(final[2])+float(final[3]))/3.00
print '%.2f' %avg
