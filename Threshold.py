#the program to sum corresponding no un elements in list and find the greatest sum less than the thresholdd
n=int(raw_input('How many elements'))
t=int(raw_input('Threshold'))
arr=raw_input("enter the nos")
arr=arr.split()
newarr=[]
print arr
for x in range(0,n):
	sum=int(arr[x])
	for j in range(x+1,n):
		sum=sum+int(arr[j])
		if sum<t:
			newarr.append(sum)
print newarr
print max(newarr)


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input('No of elements?:'))
t=int(raw_input('Threshold value?:'))
a=raw_input('Enter array of number')
peices=a.split()
max_sum=[]
final_sum=[]
for x in range(0,n-1):
	sum=0
	for i in range(x,n-1):		
		sum=sum+int(peices[i])
		if sum+int(peices[i+1])>t: 
			max_sum.append(sum)


for i in max_sum:
		if i<t:
			final_sum.append(i)
			
if len(final_sum)==0:
	print 0
else:
	print max(final_sum)		
