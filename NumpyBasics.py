# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 09:25:36 2018

@author: U40MV02
"""

import numpy as np
# Generate random values, for use in populating the matrix and vector
from random import gauss

# Native Python, using lists
n=5
A_py = [gauss(0, 1) for i in range(n*n)] # Assume: Column-major
x_py = [gauss(0, 1) for i in range(n)]

print (np.array([1,2,3]))
print (np.eye(5))
print (np.empty((3,5)))
a=np.arange(100)
print (a)
b=np.array([[1,2,3],[4,5,6]])
print (b)
print (b.ndim)
print (b.shape)
print np.zeros((3,4))
print np.zeros((3,4))
print np.ones((3,4))
print np.eye((3))
print (np.diag([1,2,3]))
print np.empty((3,4))

#A_py=np.reshape(A_py,(n,n),order='F')
#x_py=np.reshape(x_py,(1,n),order='F')

#print (A_py)
print ('*')
#print (x_py)

C1 = [[0, 1, 2, 3],
      [4, 5, 6, 7],
      [8, 9, 10, 11]]

C2 = [[12, 13, 14, 15],
      [16, 17, 18, 19],
      [20, 21, 22, 23]]

C=np.array([C1,C2])
print (C)
Z= np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])

print (Z)
print '****'
print (Z[:,2])  #Red
print (Z[0,3:5]) #Orange
print (Z[4:6,4:6])  # Cyan
print (Z[2::2,::2])

a1=np.array([[1,2,3],
    [4,5,6],
    [7,8,9]])

b1=np.array([1,1,1])
print (a1.dot(b1))