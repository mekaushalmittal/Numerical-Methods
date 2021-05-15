import numpy as np 
def printValues(xk, xk_next, fk, fk_next, num=0):
    print("\nx" + str(num) + ": ", xk)
    print("x" + str(num+1) + ": ", xk_next)
    print("fk" + str(num) + ": ", fk)
    print("fk" + str(num+1) + ": ", fk_next)
    print()
    

def regulaFalsiMethod(f, a0, b0, iterations=5, enablePrint=True):
    fk = f(a0)
    fk_next = f(b0)
    xk = a0 
    xk_next = b0
    for i in range(iterations):
        x = xk_next - ((xk_next - xk)/(fk_next - fk))*fk_next 
        f_ = f(x)
        if f_*fk < 0:
            xk_next = x 
            fk_next = f_ 
        elif f_*fk_next < 0:
            xk = xk_next 
            xk_next = x 
            fk = fk_next
            fk_next = f_
        else:
            xk = xk_next 
            xk_next = x 
            fk = fk_next 
            fk_next = f(xk_next)
        if enablePrint:
            printValues(xk, xk_next, fk, fk_next)
    return x

if __name__ == "__main__":
    def f(x):
        return np.cos(x) - x*np.exp(x)
    a0 = 0
    b0 = 1 
    root_approx = regulaFalsiMethod(f, a0, b0)
    print("Approximate Root: ", root_approx)
    print("Error: ", f(root_approx))