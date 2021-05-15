import numpy as np 

def diagonalMatrixInverse(D):
    out = np.zeros(D.shape)
    for i in range(D.shape[0]):
        out[i][i] = 1./D[i][i]
    return out 

def getWOpt(U, D_inv, L, enablePrint=True):
    R = np.matmul(D_inv, L)
    C = np.matmul(D_inv, U)
    B = - (R + C)
    if enablePrint:
        print("R: ", R)
        print("C: ", C)
        print("B: ", B)
    return 2/(1 + np.sqrt(1 - max(abs(np.linalg.eigvals(B)))**2))

def sor(x0, A, b, iter, enablePrint=True):
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
    w = getWOpt(U, D_inv, L)
    aux = np.linalg.pinv(D + w*L)
    H = np.matmul(aux, ((1-w)*D - w*U))
    c = np.matmul(w*aux, b)
    if enablePrint:
        print("L: ", L)
        print("D: ", D)
        print("U: ", U)
        print("D-inverse: ", D_inv)
        print("w: ", w)
        print("(D + w x L)-inverse: ", aux)
        print("H: ", H)
        print("c: ", c)
        print("w_opt:", w)
        print()
    x = x0
    for i in range(iter):
        r = b - np.matmul(A,x)
        v = np.matmul(w*aux, r)
        x = np.matmul(H, x) + c
        if enablePrint:
            print("r" + str(i + 1) + ": ", r)
            print("v" + str(i + 1) + ": ", v)
            print("x" + str(i + 1) + ": ", x)
            print()
    return x

if __name__ == "__main__":
    A  = np.array([[3, 2, 0],
                [2, 3,-1],
                [0, -1, 2]])
    b  = np.array([4.5, 5, -.5]).T
    x0 = np.array([0, 0, 0]).T
    x  = sor(x0, A, b, 5)
