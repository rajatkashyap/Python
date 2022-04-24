'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

str=raw_input("Enter input")
l=str.split()
d=0
c=0
for i in str:
	if i.isdigit():
		d+=1
	if i.isalpha():
		c+=1
		
print d
print c
		