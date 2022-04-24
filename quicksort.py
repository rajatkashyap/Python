def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
		pivot = array[0]
		print pivot
		for x in array:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
        # Don't forget to return something!
		print less
		print equal
		print greater
		print '*'*10
		return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print sort([12,4,5,9,16])