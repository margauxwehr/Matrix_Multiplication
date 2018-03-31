# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:56:38 2018

@author: bo
"""

#Spark 

# Example of A.txt B.txt used here are : 

#A.txt               B.txt 
# 1 1 7              1 1 3
# 1 2 6              1 2 9 
# 2 2 5              2 1 4
#                    2 2 8


    (3 9)
     4 8
(7 6 45 111
 0 5) 20 40


#i,j: int; v: float

A = sc.textFile("/Users/margaux.wehr/Documents/MAP533DatabaseManagement/Project final/A1.txt").map(lambda x : x.split(' ')) # [[1,1,7], [1,2,5]]
A = sc.textFile("/Users/margaux.wehr/Documents/MAP533DatabaseManagement/Project final/A1.txt").map(lambda x : x.split(' ')).map(lambda x: (int(x[1]), (int(x[0]), float(x[2]))))
# A becomes [ (1, [1,7]), (2, [1,6]), (2, [2,5]) ]

B = sc.textFile("/Users/margaux.wehr/Documents/MAP533DatabaseManagement/Project final/B1.txt").map(lambda x : x.split(' ')).map(lambda x: (int(x[0]), (int(x[1]), float(x[2]))))
# B becomes [ (1, [1,3]), (1, [2,9]), (2, [1,4]), (2, [2,8]) ]
 

join = A.join(B) # [(1,([1,7],[1,3])), (1,([1,7],[2,9])), (2([1,6],[1,4])), (2,([1,6],[2,8])), (2,([2,5],[1,4])), (2([2,5],[2,8])) ]

grouped= join.map(lambda x :((x[1][0][0], x[1][1][0]), x[1][0][1]*x[1][1][1])).reduceByKey(lambda x,y : x+y)

# [((1,1), 21+24), ((1,2), 63+48), ((2,1), 20), ((2,2), 40)]
