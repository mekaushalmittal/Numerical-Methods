import numpy as np 

def powerMethod(A, iter, v=None, getMax = True, enablePrint=True):
    if not getMax:
        A = np.linalg.pinv(A)
    if not v:
        v = np.ones(A.shape[0])
    for i in range(iter):
        y = np.matmul(A, v)
        m = np.max(abs(y))
        v_prev = v
        v = y/m 
        lamb = abs(np.divide(y, v_prev))
        if enablePrint:
            print("y" + str(i + 1) + ": ", y)
            print("mu" + str(i + 1) + ": ", m)
            print("v" + str(i + 1) + ": ", v)
            print("lambda" + str(i + 1) + ": ", lamb)
            print()
    lamb = np.max(abs(lamb))
    if not getMax:
        lamb = 1/lamb
    a = abs(np.linalg.det((A + lamb*np.identity(A.shape[0]))))
    b = abs(np.linalg.det((A - lamb*np.identity(A.shape[0]))))
    if a < b:
        return -lamb, v_prev
    else:
        return lamb, v_prev

if __name__ == "__main__":
    A  = np.array([[1, 0, 0],
                [1, 1, 0],
                [1, 1, 1]])
    A  = np.linalg.pinv(np.matmul(A, A.T))
    print(A)
    v  = np.array([6, -7, 3])
    lamb, v = powerMethod(A, 10, getMax=False)
    print(lamb)