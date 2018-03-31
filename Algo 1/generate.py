#!/usr/bin/env python
import numpy as np
import sys

import timeit

start = timeit.default_timer()

#argv[0] is the script name
_, filename, m, n, p = sys.argv

#Random values in a given shape from a uniform distribution over [0, 1).

M = np.random.rand(int(m), int(n))
N = np.random.rand(int(n), int(p))
M = -np.log(M).round(3)
N = -np.log(N).round(3)

f = open(filename, 'w')

#dimension of two matrices 
f.write('%s %s%s' % (m, n, '\n'))
f.write('%s %s%s' % (n, p, '\n'))


#two matrices
for i in M:
    f.write(' '.join(map(str, i)))
    f.write('\n')

for i in N:
    f.write(' '.join(map(str, i)))
    f.write('\n')

f.close



stop = timeit.default_timer()

print(stop - start)

#

#rdd =sc.textFile(hdfs://PATH)

#rdd.saveToTextFile(hdfs://OUPUT_PATH)