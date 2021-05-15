import numpy as np

def doolittleMethod(mat, enablePrint=True):
    n = len(mat)
    lower = [[0 for x in range(n)]
    		for y in range(n)]
    upper = [[0 for x in range(n)]
    		for y in range(n)]
    for i in range(n):
        for k in range(i, n):
        	sum = 0
        	for j in range(i):
        		sum += (lower[i][j] * upper[j][k])
        	upper[i][k] = mat[i][k] - sum
        for k in range(i, n):
        	if (i == k):
        		lower[i][i] = 1 # Diagonal as 1
        	else:
        		sum = 0
        		for j in range(i):
        			sum += (lower[k][j] * upper[j][i])
        		lower[k][i] = ((mat[k][i] - sum) / upper[i][i])
        if enablePrint:
            print("L" + str(i + 1) + ": ", np.asarray(lower))
            print("U" + str(i + 1) + ": ", np.asarray(upper))
    return np.asarray(lower), np.asarray(upper)

if __name__ == "__main__":
    A = [[1, 1, -1],
        [2, 3, 5],  
        [3, 2, -3]]
    lower, upper = doolittleMethod(A)
