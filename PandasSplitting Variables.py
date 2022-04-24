# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:23:44 2018

@author: U40MV02
"""

import pandas as pd
import re
from IPython.display import display

table3 = pd.read_csv('table3.csv')


def default_splitter(text):
    """Searches the given spring for all integer and floating-point
    values, returning them as a list _of strings_.
    
    E.g., the call
    
      default_splitter('Give me $10.52 in exchange for 91 kitten stickers.')
      
    will return ['10.52', '91'].
    """
    fields = re.findall('(\d+\.?\d+)', text)
    return fields

def separate(df, key, into, splitter=default_splitter):
    """Given a data frame, separates one of its columns, the key,
    into new variables.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns
    def apply_splitter(text):
        txt=default_splitter(text)

        d={into[i]:f for i,f in enumerate(txt)}
        print d
         
        return pd.Series(d)
    
    fixed_vars=df.columns.difference([key])
    #print fixed_vars
    txt=df[key].apply(apply_splitter)
    main=df[fixed_vars].copy()
    return pd.concat([main,txt],axis=1)


print("=== Recall: table3 ===")
display(table3)

tibble3 = separate(table3, key='rate', into=['cases', 'population'])
print("\n=== tibble3 = separate (table3, ...) ===")
display(tibble3)
print '*'*10

#print (type(tibble3))
def str_join_elements(x, sep=""):
    assert type(sep) is str
    return sep.join([str(xi) for xi in x])


def unite(df, cols, new_var, combine=str_join_elements):
    print ("HI")
    keep_vars=df.columns.difference(cols)
    main_df=df[keep_vars].copy()
    other_df=df[cols].copy()
    print other_df
        
    other_df['xyz']=other_df.apply(combine,axis=1)
    #other_df=pd.Series(other_df)
    #other_df.columns=['one']
    print other_df
    for c in cols:
        del other_df[c]
    print other_df
    other_df.rename(columns={other_df.columns[0]:new_var},inplace=True)
    print other_df
   #other_df1.columns=['one']
   #print other_df1
    #other_df1.rename(columns={other_df1.columns[0]:new_var},inplace=True)
    #other_df1.columns=[new_var]
    #print other_df1
    #print main_df
    return pd.concat([main_df,other_df],axis=1)



table3_again = unite(tibble3, ['cases', 'population'], 'rate',combine=lambda x: str_join_elements(x, "/"))
display(table3_again)


