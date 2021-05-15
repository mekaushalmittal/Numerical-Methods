import numpy as np 

def evaluateF(a, b, N, f):
    h = getH(a, b, N)
    return [f(a+i*h) for i in range(N+1)]

def getH(a, b, N):
    return (b-a)/N

def trapezoidalIntegrate(a, b, N, f, enablePrint=True):
    h = getH(a, b, N)    
    f = evaluateF(a, b, N, f)
    if enablePrint:
        print("h: ", h)
        for i in range(len(f)):
            print("f"+str(i)+": ", f[i])
    out = f[0] + f[-1] 
    for i in range(1, len(f)-1):
        out = out + 2*f[i]
    return (h/2) * out 

if __name__ == "__main__":
    def f(x):
        return x/(x**3 + 10)
    N = 8
    a = 0
    b = 1
    print("N: ", N)
    I = trapezoidalIntegrate(a, b, N, f)
    print("I: ", I)
    