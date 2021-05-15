import numpy as np 

def getH(x):
    return x[1] - x[0]

def getBackwardDifferences(g):
    out = [g[-1]]
    temp = [each for each in g]
    for i in range(len(temp)-1):
        temp2 = [temp[i+1]-temp[i] for i in range(len(temp)-1)]
        out.append(temp2[-1])
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


def newtonBackward(x0, g, x):
    h = getH(x0)
    fn_arr = getBackwardDifferences(g)
    u = (x-x0[-1])/h 
    u_ = -u
    out = 0
    for i in range(0, len(fn_arr)):
        out = out + (-1)**i*combination(u_,i)*fn_arr[i]
    return out 

if __name__ == "__main__":
    x0 = [0, 1, 2, 4, 5, 6]
    g = [1, 14, 15, 5, 6, 19]
    x = 3
    fx = newtonBackward(x0, g, x)
    h = getH(x0)
    fn_arr = getBackwardDifferences(g)
    print("Given x: ", x0)
    print("Given f(x): ", g)
    print("Given x at which to evaluate: ", x)
    print("Backward differences: ")
    for i in range(len(fn_arr)):
        print("\t(▽^"+str(i)+")fn: ", fn_arr[i]) 
    print("Obtained f(x): ", fx)