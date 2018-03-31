# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:44:23 2018

@author: bo
"""

import glob
#import sys


for file in glob.glob("*.txt"):
    if file == "A50.txt" :
        with open(file) as f:
            for line in f:
                i,j,v=line.split(' ')
                v=float(v)
                i,j=map(int,[i,j])
                print('%s\t%s' % ([j,"A"],[i,v]))
    elif file == "B50.txt":
        with open(file) as f:
            for line in f:
                i,j,v=line.split(' ')
                v=float(v)
                i,j=map(int,[i,j])
                print('%s\t%s' % ([i,"B"],[j,v]))