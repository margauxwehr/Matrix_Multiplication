#!/usr/bin/python

import sys
import ast

current_cid = None
cid = None
current_mid = None
mid = None
A_box = list()

# The purpose of this reducer is to match keys and do operation on their associated values
# For instance, ([1, "A"],[2, 7]) and ([1, "B"],[2, 9]) should be matched, because they have the same key which is 1.
# THe operation to do is to return ((2,2) 63), which means 63 will be put into the cell (2,2) of result matrix.

for line in sys.stdin:
    pair = line.strip().split('\t') # split the read line by space.
    pair[0] = list(ast.literal_eval(pair[0])) #convert it into list type
    pair[1] = list(ast.literal_eval(pair[1]))
    cid = pair[0][0] # cid is the first key meaning the column index
    mid = pair[0][1] # mid is the second key meaning the matrix index, it will be either A or B 

    if current_cid == None:  # if it is the begining of the lecture
        current_cid = cid    
        A_box.append(pair[1])
        # A_box is used to contain values which have [cid, "A"] as key.
    elif current_cid == cid:
        if mid == "A":
            A_box.append(pair[1])
        else:  # if the shift into [cid, "B"], we should multiply all the value in A_box with every vlue of [cid, "B"]
            for element in A_box:
                print('%s\t%s' % ((element[0], pair[1][0]), element[1]*pair[1][1]))
    
    elif current_cid != cid: # clean A_box, restart the process. renex current_cid.
        A_box = list()
        A_box.append(pair[1])
        current_cid = cid
        
# 
    
    
    
    
    
    
    
    
    