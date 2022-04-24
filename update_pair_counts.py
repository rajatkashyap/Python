'''Exercise 4 (update_pair_counts_test: 2 points). Start by implementing a function that enumerates all item-pairs within an itemset and updates, in-place, a table that tracks the counts of those item-pairs.

The signature of this function is:

   def update_pair_counts(pair_counts, itemset):
       ...
where you pair_counts is the table to update and itemset is the itemset from which you need to enumerate item-pairs. You may assume pair_counts is a default dictionary. Each key is a pair of items (a, b), and each value is the count. You may assume all items in itemset are distinct, i.e., that you may treat it as you would any set-like collection. Since the function will modify pair_counts, it does not need to return an object.
'''

from collections import defaultdict
from itertools import combinations # Hint!

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    for a,b in combinations(itemset,2):
    	pair_counts[(a,b)]=+1
    	pair_counts[(b,a)]=+1
    return 	pair_counts

# `update_pair_counts_test`: Test cell
itemset_1 = set("error")
itemset_2 = set("dolor")
pair_counts = defaultdict(int)

update_pair_counts(pair_counts, itemset_1)
assert len(pair_counts) == 6
update_pair_counts(pair_counts, itemset_2)
assert len(pair_counts) == 16

print('"{}" + "{}"\n==> {}'.format (itemset_1, itemset_2, pair_counts))
for a, b in pair_counts:
    assert (b, a) in pair_counts
    assert pair_counts[(a, b)] == pair_counts[(b, a)]
    
print ("\n(Passed!)")