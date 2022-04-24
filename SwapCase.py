s=raw_input()
s1=[]
for i in s:
    if i.isupper(): s1.append(i.lower())
    else: s1.append(i.upper())
z=''.join(s1)
print z


# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input().split()
print s
x='-'.join(s)


first=raw_input()
last=raw_input()
s=[first,last]
full=' '.join(s)
print "Hello %s! You just delved into python." %full