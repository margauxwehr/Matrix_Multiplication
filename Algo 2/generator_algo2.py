# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:08:13 2018

@author: bo
"""
import numpy as np
m=400
n = 400
p = 400
M = np.random.rand(int(m), int(n))
N = np.random.rand(int(n), int(p))
#print(M,N)
M = -np.log(M).round(3)
N = -np.log(N).round(3)

#print(M,N)
A = open("A400.txt", 'w')
B = open("B400.txt", 'w')
#f.write('%s %s%s' % (m, n, '\n'))
#f.write('%s %s%s' % (n, p, '\n'))
count_row = 0
count_col = 0
for row in M:
    count_row +=1
    for nb in row:
        count_col +=1 
        A.write('%s %s %s\n' % (count_row, count_col, nb))
    count_col = 0
count_row = 0    
A.close()
    #f.write(' '.join(map(str, )))
    #f.write('\n')
for row in N:
    count_row +=1
    for nb in row:
        count_col +=1 
        B.write('%s %s %s\n' % (count_row, count_col, nb))
    count_col = 0
B.close()
