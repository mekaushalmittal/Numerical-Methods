import numpy as np 

from doolittleMethod import doolittleMethod

def rutisHauserMethod(A, iter, enablePrint=True):
    for i in range(iter):
        L, U = doolittleMethod(A, enablePrint=False)
        if enablePrint:
            print("L" + str(i + 1) + ": ", L)
            print("U" + str(i + 1) + ": ", U)
            print("A" + str(i + 1) + ": ", A)
            print()
        A = np.matmul(U, L)
    return L, U


if __name__ == "__main__":
    A = np.array([[3, 1],
                [1, 1]])
    rutisHauserMethod(A, 5)