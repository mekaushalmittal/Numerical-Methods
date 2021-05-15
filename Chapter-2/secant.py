import numpy as np 
def printValues(xk, xk_next, fk, fk_next, num=0):
    print("\nx" + str(num) + ": ", xk)
    print("x" + str(num+1) + ": ", xk_next)
    print("fk" + str(num) + ": ", fk)
    print("fk" + str(num+1) + ": ", fk_next)
    print()
    

def secantMethod(f, a0, b0, iterations=5, enablePrint=True):
    fk = f(a0)
    fk_next = f(b0)
    xk = a0 
    xk_next = b0
    for i in range(iterations):
        if enablePrint:
            printValues(xk, xk_next, fk, fk_next,num=i)
        x = xk_next - ((xk_next - xk)/(fk_next - fk))*fk_next 
        xk = xk_next 
        xk_next = x 
        fk = fk_next 
        fk_next = f(xk_next)
    return x

if __name__ == "__main__":
    def f(x):
        return x**3 -x**2 -x + 1
    a0 = 0.8
    b0 = 1.2 
    root_approx = secantMethod(f, a0, b0, iterations=3)
    print("Approximate Root: ", root_approx)
    print("Error: ", f(root_approx))