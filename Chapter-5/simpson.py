import numpy as np 

def evaluateF(a, b, N, f):
    h = getH(a, b, N)
    return [f(a+i*h) for i in range(2*N+1)]

def getH(a, b, N):
    return (b-a)/(2*N)

def simpsonIntegrate(a, b, N, f, enablePrint=True):
    h = getH(a, b, N)    
    f = evaluateF(a, b, N, f)
    if enablePrint:
        print("h: ", h)
        for i in range(len(f)):
            print("f"+str(i)+": ", f[i])
    out = f[0] + f[-1] 
    for i in range(1, len(f)-1):
        if i%2 == 0:
            out = out + 2*f[i]
        else:
            out = out + 4*f[i]
    return (h/3) * out 

if __name__ == "__main__":
    def f(x):
        return np.cos(2*x)/((1.-np.square(x))**(0.5))
    N = 4
    a = -.999
    b = .999
    print("N: ", N)
    I = simpsonIntegrate(a, b, N, f)
    print("I: ", I)
