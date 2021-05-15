import numpy as np 

def diagonalMatrixInverse(D):
    out = np.zeros(D.shape)
    for i in range(D.shape[0]):
        out[i][i] = 1./D[i][i]
    return out 

def gaussSeidelIteration(x0, A, b, iter, enablePrint=True):
    L = np.zeros(A.shape)
    D = np.zeros(A.shape)
    U = np.zeros(A.shape)
    n = b.size 
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = A[i][j]
            elif i > j:
                L[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]
    D_inv = diagonalMatrixInverse(D)
    H = -np.matmul(np.linalg.pinv(D + L), U)
    c = np.matmul(np.linalg.pinv(D + L), b)
    if enablePrint:
        print("H: ", H)
        print("c: ", c)
        print()
    x = x0
    for i in range(iter):
        r = b - np.matmul(A,x)
        v = np.matmul(np.linalg.pinv(D + L), r)
        x = np.matmul(H, x) + c
        if enablePrint:
            print("r" + str(i + 1) + ": ", r)
            print("v" + str(i + 1) + ": ", v)
            print("x" + str(i + 1) + ": ", x)
            print()
    return x

if __name__ == "__main__":
    A  = np.array([[2, -1, 0],
                [-1, 2, -1],
                [0, -1, 2]])
    b  = np.array([7, 1, 1]).T
    x0 = np.array([0, 0, 0]).T
    x  = gaussSeidelIteration(x0, A, b, 5)
    Ax = np.matmul(A, x)
    print("Error: ", abs(np.sum(Ax - b)))
