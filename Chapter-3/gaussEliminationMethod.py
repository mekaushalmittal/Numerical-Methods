import numpy as np 

def backSubstitution(A):
    n = A.shape[0]
    x = [0 for i in range(n)]
    for k in range(n):
        temp = 0
        row = A[(n-1)-k]
        for i in range(k):
            temp = temp + x[-(i+1)]*row[(n-1)-i]
        x[(n-1)-k] = (row[n] - temp)/row[(n-1)-k]
    return x

def gaussElimination(A, b, enablePrint=True, partialPivot=False):
    n = A.shape[0]
    b = b.reshape(-1,1)
    A = np.hstack((A, b))
    for k in range(n):
        if partialPivot:
            max_ = abs(A[k][k])
            max_index = k
            for j in range(k+1, n):
                if abs(A[j][k]) > max_:
                    max_ = abs(A[j][k])
                    max_index = j 
            A[[k, max_index]] = A[[max_index, k]]
            if enablePrint:
                if k != max_index:
                    print("Exchanged Row: ",k, " with Row: ", max_index)
                    print(A, "\n")
        for i in range(k+1, n):
            if enablePrint:
                if A[i][k]  != 0:
                    print("R"+str(i)+" -> R"+str(i)+" - (R"+str(k)+"*"+str(A[i][k])+")/"+str(A[k][k]))
            A[i] = A[i] - (A[i][k]/A[k][k])*A[k]
        if enablePrint:
            print(A, "\n")
    x = backSubstitution(A)
    return x

if __name__ == "__main__":
    A = np.array([[1.,1.,-1.],
                  [2.,3.,5.],
                 [3.,2.,-3.]])
    b = np.array([2., -3., 6.])
    x = gaussElimination(A, b, partialPivot=True)
    print("x: ", x)