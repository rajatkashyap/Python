# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:40:46 2021

@author: U40MV02
"""

import pandas as pd
df=pd.read_csv("student-por.csv")
print (df['school'].count())
print (df.head())
df_agg=df.groupby(['school','sex'])
print (df_agg)
print (type(df_agg))


#print (type(df_agg.agg({"Walc":"sum"})))
#print (df_agg.agg({"Walc":"sum"}))
#print (df_agg[['Walc']].sum())

print (df_agg['Walc'].sum())
print (type(df_agg['Walc'].sum()))
print (type(df_agg[['Walc']].sum()))
print (df_agg['Walc'].sum())
print (df.groupby(['school','sex'],as_index=False)['Walc'].sum())    

print (df.groupby(['school','sex'],as_index=False).agg({'Walc':'sum','health':'count'}))    
