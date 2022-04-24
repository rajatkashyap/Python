import time
#t=gmtime()

print time.strptime("2010-04-20 10:07:30",'%Y-%m-%d %H:%M:%S')[0:6]
print zip([1,2,3],'Rajat')
A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print X
print zip(*X)

print localtime()
