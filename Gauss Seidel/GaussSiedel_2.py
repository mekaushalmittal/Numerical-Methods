# Implementation of Gauss-Seidel method for the example given in the book
# To solve the system of equations
# 2x - y = 7
# -x + 2y + -z = 1
# -y + 2z = 1
# using the Gauss Siedel method

import numpy as np

def arrays(A):
    D = [[A[0][0], 0, 0], [0, A[1][1], 0], [0, 0, A[2][2]]]
    D = np.array(D)
    U = [[0, A[0][1], A[0][2]], [0, 0, A[1][2]], [0, 0, 0]]
    U = np.array(U)
    L = [[0, 0, 0], [A[1][0], 0, 0], [A[2][0], A[2][1], 0]]
    L = np.array(L)
    return D, L, U 


def get_H(D, L, U):
    neg_I = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    neg_I = np.array(neg_I)

    D_temp = D+L
    D_inv = np.linalg.inv(D_temp) 
    temp_arr = np.matmul(D_inv, U)
    final_arr = np.matmul(neg_I, temp_arr)
    return final_arr

def get_C(D, b):
    D_temp = D+L
    D_inv = np.linalg.inv(D_temp) 
    final_arr = np.matmul(D_inv, b)
    return final_arr

A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
b = [7, 1, 1]

D, L, U = arrays(A)
H = get_H(D, L, U)
C = get_C(D, b)

x_0 = [0, 0, 0]
x_0 = np.array(x_0)

for i in range(3):
    temp_arr = np.matmul(H, x_0)
    x_arr = temp_arr + C
    print("x_" + str(i+1) + " = " + str(x_arr))
    x_0 = x_arr

# Submitted by Sarthak Khoche (IMT2017038)    