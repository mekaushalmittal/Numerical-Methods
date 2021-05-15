import numpy as np 

def jacobiEigenVector(A, iter, enablePrint=True):
    B = A
    S_arr = []
    for i in range(iter):
        max_ = abs(B[0][1])
        r = 0
        c = 1
        for col in range(B.shape[1]):
            for row in range(B.shape[0]):
                if row == col:
                    continue 
                if abs(B[row][col]) > max_:
                    max_ = abs(B[row][col])
                    r = row 
                    c = col
        aik = B[r][c]
        aki = B[c][r]
        aii = B[r][r]
        akk = B[c][c]
        if aii == akk:
            if aik > 0:
                theta = np.pi/4
            else:
                theta = -np.pi/4
        else:
            theta = 0.5*np.arctan(2*aik/(aii - akk))
        S = np.identity(A.shape[0])
        S[r][r] = np.cos(theta)
        S[c][c] = np.cos(theta)
        S[r][c] = -1*np.sin(theta)
        S[c][r] = np.sin(theta)
        S_arr.append(S)
        if enablePrint:
            print("B" + str(i) + ": ", B)
            print("S" + str(i) + ": ", S)
            print("Theta " + str(i) + ": ", theta)
            print()
        B = np.matmul(np.matmul(np.linalg.pinv(S), B), S)
    S = S_arr[0]
    for i in range(1, len(S_arr)):
        S = np.matmul(S, S_arr[i])
    return S

if __name__ == "__main__":
    A  = np.array([[1, 2, -1],
                [2, 1, 2],
                [-1, 2, 1]])
    S  = jacobiEigenVector(A, 5)
