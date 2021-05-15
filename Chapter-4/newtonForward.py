import numpy as np 

def getH(x):
    return x[1] - x[0]

def getForwardDifferences(g):
    out = [g[0]]
    temp = [each for each in g]
    for i in range(len(temp)-1):
        temp2 = [temp[i+1]-temp[i] for i in range(len(temp)-1)]
        out.append(temp2[0])
        temp = temp2 
    return out

def factorial(n):
    out = 1
    for i in range(1, n+1):
        out = out*i 
    return out 

def combination(u, n):
    out = 1
    for i in range(n):
        out = out * (u-i)
    return out/factorial(n)


def newtonForward(x0, g, x):
    h = getH(x0)
    f0_arr = getForwardDifferences(g)
    u = (x-x0[0])/h 
    out = 0
    for i in range(0, len(f0_arr)):
        out = out + combination(u,i)*f0_arr[i]
    return out 

if __name__ == "__main__":
    x0 = [0, 1, 2, 4, 5, 6]
    g = [1, 14, 15, 5, 6, 19]
    x = 3
    fx = newtonForward(x0, g, x)
    h = getH(x0)
    fn_arr = getForwardDifferences(g)
    print("Given x: ", x0)
    print("Given f(x): ", g)
    print("Given x at which to evaluate: ", x)
    print("Forward differences: ")
    for i in range(len(fn_arr)):
        print("\t(▽^"+str(i)+")fn: ", fn_arr[i]) 
    print("Obtained f(x): ", fx)