matrix = sc.textFile("/Users/apple/Desktop/matrix/newtest")
matrixidx = matrix.zipWithIndex()

M=matrixidx.filter(lambda x: 2<= x[1]<=3).map(lambda x:x[0]).map(lambda x: x.split(" ")).map(lambda x : [float(x[i]) for i in range(len(x)) ] ).zipWithIndex()


N=matrixidx.filter(lambda x: 4<= x[1]<=6).map(lambda x:x[0]).map(lambda x: x.split(" ")).map(lambda x : [float(x[i]) for i in range(len(x)) ] ).zipWithIndex()

M_idx = M.map(lambda x: [(i,(x[1],x[0][i])) for i in range(len(x[0]))]).flatMap(lambda x : x) #(i,j,M[ij])

N_idx = N.map(lambda x: [(x[1],(i,x[0][i])) for i in range(len(x[0]))]).flatMap(lambda x : x) #(j,k,N[jk])

join = M_idx.join(N_idx) 

join.map(lambda x: ((x[1][0][0], x[1][1][0]), x[1][0][1]*x[1][1][1]).reduceByKey(lambda x,y : x+y)