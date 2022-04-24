l=list(range(1,10))
print list(filter(lambda x:x%2==0,l))
i=[1,2,3,5]
print list(map((lambda x:x**2),i))
print list(map(lambda x:x**2,i))

print reduce((lambda x,y: x * y),l)

print reduce( (lambda x, y: x * y), [1, 2, 3, 4] )


it=1
for x in l:
    it=it*x

print it

print len(l)

def myRed(fnc,l):
    x=1
    for i in range(0,len(l)-1):
       x=fnc(x,l[i+1])
    return x

def myMap(func,seq):
    result=[]
    for i in seq: result.append(func(i))
    return result

j=myRed((lambda x,y:x*y),[1,2,3,4,5])

print myMap(lambda x:x**2,[1,2,3,4])

