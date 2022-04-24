'''Exercise 3 (make_itemsets_test: 2 points). Implement a function, make_itemsets(words). The input, words, is a list of strings. Your function should convert the characters of each string into an itemset and then return the list of all itemsets. These output itemsets should appear in the same order as their corresponding words in the input.'''

def make_itemsets(words):
	words_l=words.split()
	print words_l
	make_itemsets=[]
	for w in words_l:
		make_itemsets.append(set(w))
	return make_itemsets

print	make_itemsets("Hi how are you Rajat")



