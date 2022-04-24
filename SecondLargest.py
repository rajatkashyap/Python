n=raw_input("Enter how many nos (2<=N<=10):")
#n=raw_input()
l=raw_input("Enter nos:")
#l=raw_input()
elem=l.split()
rl=[]
intelem=[]
for i in elem:
    intelem.append(int(i))

intelem.sort(reverse=True)
print intelem
rl=list(set(intelem))
rl.sort(reverse=True)
print rl[1]
print rl[::-1]


    #.sort(reverse=True)
