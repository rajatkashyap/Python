str=raw_input('Input a string')
ln=len(str)
str1=''
str2=''
str3=''
x=1
y=0
for l in range(ln-1,-1,-1):
	str2=str2+str[l]
    
print str2
str2=''

for i in range(ln-1,-1,-1):
    	str2=str2+str[i]
print str2

for letter in str[::-1]:
	str3=str3+letter
	
while ln>0 :
	ln=ln-1
	str1=str1+str[ln]
print str1	
#print str2
#print str3

while x:
	x=raw_input('Input a no, -1 to exit')
	x=int(x)
	if x==-1: break
	y=y+x
print 'The sum is', y
	
#print reversed(str)
#print ''.join(reversed(str))
	
	