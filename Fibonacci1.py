# 	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 0,1,
nums=int(raw_input('How many numbers: '))
#fib=['0','1']
fib=[]
sum=0
for i in range(nums):
	if i ==0 or i==1:
		fib.append(str(i))
	else:
		sum=int(fib[i-2])+int(fib[i-1])
		fib.append(str(sum))
print ' '.join(fib)