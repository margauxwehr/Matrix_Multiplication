#!/usr/bin/env python

import fileinput
import sys
import timeit

start = timeit.default_timer()

Mlist = {}
Nlist = {}

# (i, k, 'M', j, Mij)) #Mij = M[ij]
# (i, k, 'N', j, Njk)) #Njk = N[jk]

for line in fileinput.input():


    line = line.strip()
    #key (i,k)
    #data: matrix, j, Mij / Njk
    key,data = line.split()
    mat,j,val = data.split(',')
    j = int(j)
    val = float(val)

    #in M matrix
    if mat == 'M':
        if key in Mlist.keys(): 
            Mlist[key].append((j, val))
        else:
            Mlist[key] = [(j, val)]
    #in N matrix 
    else: 
        if key in Nlist.keys():
            Nlist[key].append((j, val))
        else:
            Nlist[key] = [(j, val)]
    #print(Mlist)
    #print(Nlist)


# #MList: 
# {'0,0': [(0, 0.488), (1, 1.701), (2, 0.41)], 
# '0,1': [(0, 0.488), (1, 1.701), (2, 0.41)], 
# '1,0': [(0, 0.047), (1, 0.447), (2, 0.18)], 
# '1,1': [(0, 0.047), (1, 0.447), (2, 0.18)]}

## Nlist:
# {'0,0': [(0, 0.704), (1, 2.305), (2, 0.736)], 
# '0,1': [(0, 1.137), (1, 1.435), (2, 0.897)], 
# '1,0': [(0, 0.704), (1, 2.305), (2, 0.736)], 
# 1,1': [(0, 1.137), (1, 1.435), (2, 0.897)]}

#index /key: index of new matrix 
# #arr: list of pair M:(j-th row, value) N:(j-th column, value)
  
for index, tup in Mlist.items():   #items(): return key and value 

    res = 0 # intial the multiplied value 
    for j, val in enumerate(tup):
        res += val[1] * Nlist[index][j][1] # multiply t

    #print("%s %s" % (index, res))  

stop = timeit.default_timer()

#print(stop - start)
