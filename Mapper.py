# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
		data = line.strip().split("\t")
		date, time, store, item, cost, payment = data
		print data
        # Now print out the data that will be passed to the reducer
		print "{0}\t{1}".format(store, cost)
        
		if len(data)==6:
            # This is the place you need to do some defensive programming
            # what if there are not exactly 6 fields in that line?
            # YOUR CODE HERE
            
            # this next line is called 'multiple assignment' in Python
            # this is not really necessary, we could access the data
            # with data[2] and data[5], but we do this for conveniency
            # and to make the code easier to read
			date, time, store, item, cost, payment = data
            # Now print out the data that will be passed to the reducer
			print "{0}\t{1}".format(store, cost)
        
test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__