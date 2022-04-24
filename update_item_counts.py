'''Exercise 5 (update_item_counts_test: 2 points). Implement a procedure that, given an itemset, updates a table to track counts of each item.

As with the previous exercise, you may assume all items in the given itemset (itemset) are distinct, i.e., that you may treat it as you would any set-like collection. You may also assume the table (item_counts) is a default dictionary.

'''
from collections import defaultdict
from itertools import combinations 

def update_item_counts(item_counts, itemset):
	for i in itemset:
		item_counts[i]=item_counts[i]+1
		#print item_counts
	




# `update_item_counts_test`: Test cell
itemset_1 = set("error")
itemset_2 = set("dolor")

item_counts = defaultdict(int)
update_item_counts(item_counts, itemset_1)
assert len(item_counts) == 3
update_item_counts(item_counts, itemset_2)
assert len(item_counts) == 5


assert item_counts['d'] == 1
assert item_counts['e'] == 1
assert item_counts['l'] == 1
assert item_counts['o'] == 2
assert item_counts['r'] == 2

print("\n(Passed!)")