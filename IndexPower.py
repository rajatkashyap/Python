def index_power1(array, n):
    if n not in array:
        return -1
    else:
        return array[n]**n


def index_power(array, n):
    if n in range(len(array)):
        return array[n] ** n
    else:
        return -1

print index_power1([1,2,3],3)

#print index_power1([1,2,3],3)

print 5.0//2
print 'rajat'.count('a')