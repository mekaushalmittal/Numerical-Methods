import numpy as np 
def printValues(x, fx, f_x, f__x, num=0):
    print("\nx" + str(num) + ": ", x)
    print("f" + str(num) + ": ", fx)
    print("f'" + str(num) + ": ", f_x)
    print("f''" + str(num) + ": ", f__x)
    print()
    

def chebyshevMethod(f, df, ddf, x0, iterations=5, enablePrint=True):
    fx = f(x0)
    f_x = df(x0)
    f__x = ddf(x0)
    for i in range(iterations):
        if enablePrint:
            printValues(x0, fx, f_x, f__x, num=i)
        x = x0 - fx/f_x - 0.5*((fx**2)/(f_x**3))*f__x 
        x0 = x 
        fx = f(x0)
        f_x = df(x0)
        f__x = ddf(x0)

if __name__ == "__main__":
    def f(x):
        return x**3 -5*x +1
    def df(x):
        return 3*x**2 - 5 
    def ddf(x):
        return 6*x
    x0 = 0.5
    root_approx = chebyshevMethod(f, df, ddf, x0)
    print("Approximate Root: ", root_approx)
    print("Error: ", f(root_approx))