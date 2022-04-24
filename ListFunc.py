l=[1,2,3,4,10]

l.insert(3,0)
print l
l.remove(0)
print l
l.pop(1)
print l
print l.index(3)
print l.count(3)
l.reverse()
print l

for i in range(10,-1,-1):
    print i
squares = [x**2 for x in range(10)]
print squares

l1=[]
for i in [1,2,3]:
    for j in [3,1,4]:
        if (i!=j):
            l1.append((i,j))

print l1

print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

matrix = [
[1, 2, 3, 4],  [5, 6, 7, 8], [9, 10, 11, 12] ]
tm=[]
tma=[]
for i in range(len(matrix[1])):
    tm=[]
    for x in matrix:
        tm.append(x[i])
    tma.append(tm)

print tma

ll= [[row[i] for row in matrix]for i in range(len(matrix[1]))]
print ll

