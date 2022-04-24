x=int(raw_input())
y=int(raw_input())

for i in range (x):
    print '-'*(y/2-1),'.','|', '.','-'*(y/2-1)

startlist = [5, 3, 1, 2, 4]
squarelist = map(lambda x:x*x,startlist)
squarelist.sort()
print squarelist