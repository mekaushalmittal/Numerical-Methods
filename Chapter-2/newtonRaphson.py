import numpy as np 
def printValues(x, fk, dfk, num=0):
    print("\nx" + str(num) + ": ", x)
    print("fk" + str(num) + ": ", fk)
    print("fk'" + str(num) + ": ", dfk)
    print()
    

def newtonRaphsonMethod(f, df, x0, iterations=5, enablePrint=True):
    x = x0
    fk = f(x)
    dfk = df(x)
    for i in range(iterations):
        if enablePrint:
            printValues(x, fk, dfk, num = i)
        x = x - fk/dfk
        fk = f(x)
        if fk == 0:
            return x
        dfk = df(x)
    return x

if __name__ == "__main__":
    def f(x):
        return np.log(x) - (x**2 - 1)
    def df(x):
        return 1/x - 2*x
    x0 = 0.5
    root_approx = newtonRaphsonMethod(f, df, x0)
    print("Approximate Root: ", root_approx)
    print("Error: ", f(root_approx))