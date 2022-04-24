# -*- coding: utf-8 -*-
"""
 idx1 = [4, 2, 1, 0]
    coef1 = [3, 2, 2, 5]

    idx2 = [3, 2, 1, 0]
    coef2 = [4, 3, 1, 2]

    add_coef(idx1, coef1, idx2, coef2) == [3, 4, 5, 3, 7]
"""

idx1 = [4, 2, 1, 0]
coef1 = [3, 2, 2, 5]

idx2 = [3, 2, 1, 0]
coef2 = [4, 3, 1, 2]

def add_idx(idx1, idx2):
    idx=[]
    for i in idx1:
        if i not in idx:
            idx.append(i)
    for i in idx2:
        if i not in idx:
            idx.append(i)
    return sorted(idx,reverse=True)

def add_coef(idx1, coef1, idx2, coef2):
    indx=add_idx(idx1, idx2)
    coeff=[]
    print indx
    for i in indx:
        #if i in idx1:
          #  print indx.index(i)
          #  print (coef1[idx1.index(i)])
        if i in idx1:
            if i in idx2:
                #print coef1[indx.index(i)]
                coeff.append(coef1[idx1.index(i)]+coef2[idx2.index(i)])
            else:
                 coeff.append(coef1[idx1.index(i)])
        else:
            coeff.append(coef2[idx2.index(i)])
    print coeff

        
    
    

add_coef(idx1, coef1, idx2, coef2)
    
    

