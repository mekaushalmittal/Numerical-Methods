import numpy as np 
def printValues(f, a, b, m, num=0):
    print("\na" + str(num) + ": ", a)
    print("b" + str(num) + ": ", b)
    print("m" + str(num + 1) + ": ", a + (b - a)/2)
    print("f(a" + str(num) + "): ", f(a))
    print("f(b" + str(num) + "): ", f(b))
    print("f(m" + str(num+1) + "): ", f(m))
    print()

def oneIteration(f, a, b, fa, fb, num=0, enablePrint=True):
    out = [0,0,0,0]
    m = a + (b - a)/2
    fm = f(m)
    if fa*fm < 0:
        out[0] = a
        out[1] = m 
        out[2] = fa 
        out[3] = fm 
    else:
        out[0] = m 
        out[1] = b 
        out[2] = fm
        out[3] = fb 
    if enablePrint:
        printValues(f, a, b, m,num=num)
    return out 

def bisectionMethod(f, a0, b0, iterations=5, error=0.005, stopOnIteration=True, enablePrint=True):
    fa0 = f(a0)
    fb0 = f(b0)
    if not stopOnIteration:
        iterations = int((np.log(b0 - a0) - np.log(error))/np.log(2)) + 1
    for i in range(iterations):
        out = oneIteration(f, a0, b0, fa0, fb0, num=i, enablePrint=enablePrint)
        a0  = out[0]
        b0  = out[1]
        fa0 = out[2]
        fb0 = out[3]
    return a0 + (b0 - a0)/2 

if __name__ == "__main__":
    def f(x):
        return np.tan(x) + np.tanh(x)
    a0 = 2.2
    b0 = 2.4
    root_approx = bisectionMethod(f, a0, b0, stopOnIteration=False)
    print("Approximate Root: ", root_approx)
    print("Error: ", abs(f(root_approx)))