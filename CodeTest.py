## input no of elements
# input elements
# input threshold

#3 4 5 6 t -10

n=raw_input("Enter no of elements:")
a=raw_input("Enter elements:")
t=int(raw_input("Enter threshold:"))
elements=a.split()
print elements
sum=0
maxlist=[]

for x in range(0,len(elements)):
    sum=0
    for y in range(x, len(elements)):
        if (sum + int(elements[y]) < t):
            sum+=int(elements[y])
            if (y==len(elements)-1):
                maxlist.append(sum)
        else:
            maxlist.append(sum)
            break

if(len(maxlist)==0): print 0
else: print "Max is:",max(maxlist)

