# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:31:40 2018

@author: U40MV02
"""

import pandas as pd
from IPython.display import display
import numpy as np

movies=pd.read_csv('movies.csv')
#display(movies.head())
#print(movies.index)
#print(movies.describe)
#print (movies[['movie_id','genre','title']].head(3))
#print (movies[['movie_id','genre','title']].iloc[4:10])
#print (movies.loc[1])
#print movies.apply(np.sum)

df = pd.DataFrame([[4, 9],] * 3, columns=['A', 'B'])
print df
print df.apply(np.sum)
print df.apply(np.sum,axis=1)
col_r= sorted(df.columns,reverse=True)
df1=df[col_r].copy()
print df1
print df1.columns
print df.columns
print df.index
print df.values
print df.T
print df.describe()

dates = pd.date_range('20130101', periods=6)
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df1

print df1.sort_index(axis=1,ascending=False)
print df1.loc['2013-01-01']
print df1.loc['2013-01-01':'2013-01-03',['A']]

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

#canonicalize_tibble(canonical_in)

def tibbles_are_equivalent(A, B):
    """Given two tidy tables ('tibbles'), returns True iff they are
    equivalent.
    """
    A1=canonicalize_tibble(A)
    B1=canonicalize_tibble(B)
    return A1.equals(B1)
