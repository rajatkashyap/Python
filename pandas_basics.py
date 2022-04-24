# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:44:05 2018

@author: u40mv02
"""

import pandas as pd
#from IPython.display import display
#import numpy as np

movies=pd.read_csv('movies.csv')
print (movies)
s=pd.Series(movies['movie_id'])
print s
print type(s)
print (s.index)
d = {'b' : 1, 'a' : 0, 'c' : 2}
s1=pd.Series(d)
print s1
print (s1.index)
print (movies['movie_id'].head())
print (movies[['movie_id','genre']].head())
print (movies.iloc[1:5,[0,2]])
print (movies[movies['movie_id']==5])
print (movies.index.max())
print (movies['genre'].unique())
print (movies.sort_values(by='movie_id',ascending=False).head())
movies['xyx']=11
print movies.head(10)
del movies['xyx']
movies.rename(columns={'genre':'Genre'},inplace=True)
print movies.head(1)
movies.rename(columns={'Genre':'genre'},inplace=True)
print movies.head(1)
movies1=movies['movie_id'].copy
#movies1['Hero']='Rajat'
print (movies1)
print (pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))
print (s[s>s.mean()])
print (s[[1,3,5]])
print (movies.movie_id)
print (movies[:5])
#print (movies.index)
print (movies.loc[30:33,['movie_id','genre']])
#print (movies.loc[30:33,movies.loc[:'movie_id']>30]    )
col_vals=['genre']
movies_2=movies.columns.difference(col_vals)
print movies[movies_2]
new=pd.Series(['a','b','c','d'],[2,3,4,5])
new1=pd.Series([2,-3,-4,5])
print (new)
print (new[2])
#x=(new/2==0)
#print (new[x])
print new1.apply(abs)
print new1.apply(lambda x:x^2)

cafes = pd.DataFrame({'name': ['east pole', 'chrome yellow', 'brash', 'bar crema', '3heart', 'spiller park pcm'],
                   'zip': [30324, 30312, 30318, 30030, 30306, 30308],
                   'poc': ['jared', 'kelly', 'matt', 'julian', 'nhan', 'dale']})
print("type:", type(cafes))
print(cafes)
print(type(cafes['zip']))
print cafes.columns
assert all(cafes['zip'].index==cafes.index) , "Not working"
print (new.loc[2]) #Prints s
print (new.iloc[2]) # Prints c
cafes3=cafes.copy()
print (cafes3)
cafes3['price']='$$'
fancy=cafes3['zip'].isin([30306, 30308])
print (fancy)
cafes3.loc[fancy,'price']+='$'
print cafes3.loc[fancy,]
print (cafes3)
cafes3.index=cafes3['name']
print (cafes3)
cafes3.index.name=None
print (cafes3)
print (cafes3.apply(lambda x:type(x)))
print (cafes3.apply(lambda x:type(x),axis=1))
