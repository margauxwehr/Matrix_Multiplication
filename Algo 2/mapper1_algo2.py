#!/usr/bin/python

#import os
import glob
#import sys


for file in glob.glob("*.txt"):   #locate files of txt format
    if file == "A.txt" : 
        with open(file) as f:
            for line in f:
                i,j,v_A=line.split(' ') #split by space
                v_A=float(v_A)
                i,j=map(int,[i,j])
                print('%s\t%s' % ([j,"A"],[i,v_A])) #output of mapper if the line is from A.txt
                # Here [j,"A"] will be a key in next reducer phase.
    elif file == "B.txt":
        with open(file) as f:
            for line in f:
                i,j,v_B=line.split(' ')
                v_B=float(v_B)
                i,j=map(int,[i,j])
                print('%s\t%s' % ([i,"B"],[j,v_B])) #output of mapper if the line is from B.txt
                # Here [i,"B"] will be a key in next reducer phase.
                # [j, "A"] and [i, "B"] are keys, if i and j are equal, then their associated value
                #[i, v_A] and [j, v_B] will be operated.