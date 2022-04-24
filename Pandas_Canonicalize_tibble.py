# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:46:47 2018

@author: U40MV02
"""

canonical_in_csv = """,c,a,b
2,hat,x,1
0,rat,y,4
3,cat,x,2
1,bat,x,2"""

with StringIO(canonical_in_csv) as fp:
    canonical_in = pd.read_csv(fp, index_col=0)
print("=== Input ===")
display(canonical_in)
print("")
    
def canonicalize_tibble(X):
    # Enforce Property 1:
    var_names = sorted(X.columns)
    Y = X[var_names].copy()
    Y.sort_values(by=var_names,inplace=True)
    #Y1=Y.sort_values(by=['a','b','c'])
    Y2=Y.reset_index(drop=True)
    
    return (Y2)