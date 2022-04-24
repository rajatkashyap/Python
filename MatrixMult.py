m1=[[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]
m2=[[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]
tm=[]
sm=[]

'''
1 2 3	1 2 3
4 5 6   4 5 6
7 8 9   7 8 9
'''
for i in range(len(m2)):
	for j in range(len(m2[0])):
		tm.append(m2[j][i])
print tm

for i in range(len(m1)):
	summ=0
	for j in range(len(m1[0])):
		summ=summ+int(m1[i][j])*int(m2[j][i])
	sm.append(summ)
print sm