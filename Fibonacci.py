# Fibonacci series
# 	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
num=int(raw_input("How many number :"))

def fibonacci(num):
	if num==0 or num==1:
		return num
	else:
		return fibonacci(num-1) + fibonacci(num-2)

for i in range(0,num):
	print fibonacci(i)


	
