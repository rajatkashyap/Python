# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:35:47 2018

@author: U40MV02
"""

def melt(df, col_vals, key, value):
    assert type(df) is pd.DataFrame
    keep=df.columns.difference(col_vals)
    m_sec=[]
    for c in col_vals:
        mel_c=df[keep].copy()
        mel_c[key]=c
        mel_c[value]=df[c]
        m_sec.append(mel_c)
    melted=pd.concat(m_sec)
    melted.reset_index(drop=True,inplace=True)
    return (melted)
table4a = pd.read_csv('table4a.csv')
display(table4a)
melt(table4a, col_vals=['1999', '2000'], key='year', value='cases')