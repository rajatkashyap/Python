from collections import defaultdict
from itertools import combinations 



# `filter_rules_by_conf_test`: Test cell
'''pair_counts = {('man', 'woman'): 5,
               ('bird', 'bee'): 3,
               ('red fish', 'blue fish'): 7}
item_counts = {'man': 7,
               'bird': 9,
               'red fish': 11}
rules = filter_rules_by_conf (pair_counts, item_counts, 0.5)
print rules'''

def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {}
    for a,b in pair_counts:
    	print ("print pair")
    	print a,b
    	print  pair_counts[(a,b)]
    	print item_counts[a]
    	conf=pair_counts[(a,b)]*1.0/(item_counts[a])*1.0
    	print conf
    	if conf>=threshold:
    		print ("adding rule")
    		rules[(a,b)]=conf
    return rules

def update_pair_counts(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    for a,b in combinations(itemset,2):
    	pair_counts[(a,b)]=pair_counts[(a,b)]+1
    	pair_counts[(b,a)]=pair_counts[(b,a)]+1
    #return 	pair_counts

def update_item_counts(item_counts, itemset):
	for i in itemset:
		item_counts[i]=item_counts[i]+1
		#print item_counts

def find_assoc_rules(receipts, threshold):
	p=defaultdict(int)
	i=defaultdict(int)
	for r in receipts:
		update_pair_counts(p,r)
		update_item_counts(i,r)
	rules1= filter_rules_by_conf(p,i,threshold)
	return rules1



receipts = [set('abbc'),set('ac'), set('a')]
#receipts=[set('ac')]
rules = find_assoc_rules(receipts, 0.6)

print("Original receipts as itemsets:", receipts)
print("Resulting rules:")
print (rules)

assert ('a', 'b') not in rules
assert ('b', 'a') in rules
assert ('a', 'c') in rules
assert ('c', 'a') in rules
assert ('b', 'c') in rules
assert ('c', 'b') not in rules

print("\n(Passed!)")

