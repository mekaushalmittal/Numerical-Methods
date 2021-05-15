import numpy as np 
import shutil
from trapezoidal import trapezoidalIntegrate

def printValues(m, I_arr):
    print("Order " + str(2*(m)) + " values: ")
    for i in range(len(I_arr)):
        if m == 1:
            print("[ h /",str(2**i),"]: ",I_arr[i])
        else:
            print(">> ",I_arr[i])
    print()

def update(m, I):
    return [((4**m)*I[i+1] - I[i])/(4**m - 1) for i in range(len(I)-1)]

def romberg(N_arr, a, b, f, enablePrint=True):
    I_arr = [trapezoidalIntegrate(a, b, each, f, enablePrint=False) for each in N_arr]
    m = 1
    while len(I_arr) > 1:
        if enablePrint:
            printValues(m, I_arr)
        I_arr = update(m, I_arr)
        m = m + 1
    printValues(m, I_arr)
    return I_arr[0]
    

if __name__ == "__main__":
    def f(x):
        return np.cos(2*x)/((1-np.square(x))**(0.5))
    N_arr = [2, 4, 8]
    a = -.999
    b = .999
    print("Different values of N: ", N_arr)
    I = romberg(N_arr, a, b, f)
    print("Improved Result: ", I)
    try: shutil.rmtree("__pycache__")
    except: pass