#!/usr/bin/env python
import fileinput
import sys 
import timeit

start = timeit.default_timer()

#intiative # of row, column of N and M 
Mrow = 0
Mcol = 0
Nrow = 0
Ncol = 0

#pos1: 2,3 
#pos2: 3,2
#pos3: the first row of matrix M 
#....
#pos5: the first row of matrix N 
#
#pos7: the last row of matrix N 

for pos, line in enumerate(fileinput.input(),1):

    line = line.strip()
    # print("pos",pos)
    # print("line",line)

    #get the dimension of M
    if pos == 1:
        Mrow, Mcol = map(int, line.split()) 

    #get the dimension of N
    elif pos == 2:
        Nrow, Ncol = map(int, line.split())
        assert Mcol == Nrow 

    #the content of matrix M, here, [pos3,pos4]
    elif pos <= (2 + Mrow):
        i = pos - 2 #set i from 1 
        #get the i-th row of matrix M
        cols = map(float, line.split())
        
        #for each row, give the index of columns 
        #give the j=0,1,2 for the i=1 row 0.976 0.361 0.345
        for j, Mij in enumerate(cols,1):
            #print("M",j,Mij)
            for k in range(1, Ncol+1):
                print("%s,%s %s,%s,%s" % (i, k,'M', j, Mij)) #Mij = M[ij]

    #the content of matrix N, here, [pos5,pos7]
    else:
        j = pos - (2 + Mrow) # set j from 1
        cols = map(float, line.split())

        #for each row, give the index of columns 
        for k, Njk in enumerate(cols,1):
           # print("N",k, Njk)
            for i in range(1, Mrow+1):
                print("%s,%s %s,%s,%s" % (i, k, 'N', j, Njk)) #Njk = N[jk]
                #M*N: ik, sort by the first two indeces
                #under the group, then check j, multiply 



stop = timeit.default_timer()

#print(stop - start)

