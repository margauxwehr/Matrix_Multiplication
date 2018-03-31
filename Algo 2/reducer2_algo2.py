# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:58:17 2018

@author: bo
"""

# In this step, we are going to sum up all value which are put into the same cell out result matrix.
# The opeation to do is a simple reduceByKey using addtion fonction.


import sys
import ast
current_key = None
key = None
Sum = 0
current_sum = 0

result = open("Result1.txt", 'w')

for line in sys.stdin:
    (key,value) = line.strip().split('\t') # split the read line by space.
    key = ast.literal_eval(key)
    value = float(value)
    if current_key == None:  # Initiation, assign current_key and Sum
        current_key = key
        Sum = value         
        
    elif current_key == key: # Sum up value having the same key
        Sum += value
        
    else:
        # Once switched into another key, print the result out and write it intp the result file.
        result.write('%s\t%s\t%s\n' % (current_key[0],current_key[1], Sum))
        #print(current_key[0],current_key[1], Sum)
        current_key = key
        Sum = value
# Don't fprget the last retained Sum to output.
#print(current_key[0],current_key[1], Sum)
result.write('%s\t%s\t%s\n' % (current_key[0],current_key[1], Sum))
result.close() # Don't forget to close opened file.