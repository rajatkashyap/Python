name = 'Parag'
if name == 'Rajat':
    print 'yes'
elif name == 'Parag':
    print 'no'
else:
    print 'wrong'

x = int(raw_input("Enter the no of elements"))
l1 = []
'''y1=[]
z1=[]
z1=raw_input("Enter elements").split()
assert isinstance(z1, object)
print max(z1)'''


for i in range(1, x+1):
    print i
    l1.append(i)

print l1
print len(l1)

print l1.pop()

print l1
print ' '.join(l1)
print '#'.join(l1[1:3])