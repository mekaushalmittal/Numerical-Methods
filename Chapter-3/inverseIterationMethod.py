import numpy as np 

def inverseIteration(A, B0, iter, enablePrint=True):
    I = np.identity(A.shape[0])
    B = B0
    for i in range(iter):
        if enablePrint:
            AB = np.matmul(A, B)
            print("B: ", B)
            print("Error: ", np.matmul((I-AB), (I-AB)))
            print()
        B = np.matmul(B, 2*I - AB)
    return B

if __name__ == "__main__":
    A  = np.array([[1, 1],
                [1, 2]])
    B0 = np.array([[1.8, -0.9],
                [-0.9, 0.9]])
    B  = inverseIteration(A, B0, 5)
