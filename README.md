# Matrix_Multiplication

We consider the problem of multiplying two big matrixes An,m and Bm using two algorithms in both MapReduce and Spark.
We consider the simple textual representation of a matrix where the value v for Ai,j is represented by a text line ‘i j v’. Only non-zero values will have a line in the textual file representing a matrix.
We perform experimental evaluation by considering 5 couples of matrices of increasing sizes, by doubling the sizes from a pair of matrix to the subsequent pair.

Our code includes: 

Algo 1 folder, containing: 

generator (generator.py) to generate the matrices under the folder test.txt; MapReduce (mapper.py + reducer.py); Spark code (spark1.py)

Algo 2 folder, containing:

generator (generator_algo2.py) generating 2 matrices A.txt and B.txt; mapper and 2 reducers to run in MapReduce (mapper1_algo2.py; reducer1_algo2.py; reducer2_algo2.py); mapper to scale on bigger matrices, taking the example of a 50 x 50 matrice (mapper1_algo2_50x50.py); Spark code (Spark_algo2.py)


