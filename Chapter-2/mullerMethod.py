import numpy as np 
def printValues(h, lamb, g, c, lamb2, x, f, num=0):
    print("\nh" + str(num) + ": ", h)
    print("lambda" + str(num) + ": ", lamb)
    print("g" + str(num) + ": ", g)
    print("c" + str(num) + ": ", c)
    print("lambda" + str(num+1) + ": ", lamb2)
    print("x" + str(num+1) + ": ", x)
    print("f" + str(num+1) + ": ", f)
    print()
    

def mullerMethod(f, x0, x1, x2, iterations=5, enablePrint=True):
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    if enablePrint:
        print("f0:", f0)
        print("f1:", f1)
        print("f2:", f2)
    for i in range(iterations):
        h1 = x1 - x0 
        h2 = x2 - x1 
        lambda2 = h2/h1 
        delta2 = 1 + lambda2
        g2 = f0*lambda2**2 - f1*delta2**2 + (lambda2 + delta2)*f2 
        c2 = lambda2*(lambda2*f0 - delta2*f1 + f2) 
        lambda3 = -(2*delta2*f2)/(g2 + np.sign(g2)*np.sqrt(g2**2 - 4*delta2*f2*c2))
        x3 = x2 + (x2 - x1)*lambda3
        f3 = f(x3)
        x0 = x1 
        x1 = x2 
        x2 = x3 
        f0 = f1 
        f1 = f2 
        f2 = f3 
        if enablePrint:
            printValues(h2, lambda2, g2, c2, lambda3, x3, f3, num=i+2)
    return x3 

if __name__ == "__main__":
    def f(x):
        return x**3 -x**2 -x + 1
    x0 = 0.6
    x1 = 0.8
    x2 = 1.2
    root_approx = mullerMethod(f, x0, x1, x2)
    print("Approximate Root: ", root_approx)
    print("Error: ", f(root_approx))