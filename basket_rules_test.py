from itertools import combinations 
from collections import defaultdict
with open('C:/Rajat/Georgia Tech/CSE 6040 - Computing for Data Analysis/groceries.csv') as f:
	groceries_file1=f.read()
	#print groceries_file1
# Confidence threshold
THRESHOLD = 0.5
#print type(groceries_file1)
# Only consider rules for items appearing at least `MIN_COUNT` times.
MIN_COUNT = 10

#print groceries_file1
		
#g=[groceries_file1.splitlines()]
#print type(g)
#print g[1]

def update_pair_counts(pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    for a,b in combinations(itemset,2):
    	pair_counts[(a,b)]=pair_counts[(a,b)]+1
    	pair_counts[(b,a)]=pair_counts[(b,a)]+1
    return 	pair_counts

def update_item_counts(item_counts, itemset):
	for i in itemset:
		item_counts[i]=item_counts[i]+1
	
def find_assoc_rules(receipts, threshold):
	p=defaultdict(int)
	i=defaultdict(int)
	for r in receipts:
		update_pair_counts(p,r)
		update_item_counts(i,r)
	print '*' *10
	print i
	print '*' *10
	rules1= filter_rules_by_conf(p,i,threshold)
	return rules1
	print '*' *10
	#print p
	print '*' *10
	

def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {}
    for a,b in pair_counts:
    	#print ("print pair")
    	#print a,b
    	#print  pair_counts[(a,b)]
    	#print item_counts[a]
    	conf=pair_counts[(a,b)]*1.0/(item_counts[a])*1.0
    	#print conf
    	if conf>=threshold and item_counts[a]>=10:
    		#print ("adding rule")
    		rules[(a,b)]=conf
    return rules


g=groceries_file1.splitlines()
gorc=[]
for  i in g:
	#print i
	#print THRESHOLD
	
	arr=i.split(',')
	gorc.append(arr)
	#print gorc
	#g_r=find_assoc_rules(gorc,THRESHOLD)

#print gorc
g_r=find_assoc_rules(gorc,THRESHOLD)
print '*'*90		
print len(g_r)
