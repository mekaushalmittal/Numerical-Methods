def newtonRaphson(k1, F, dF, t, u, n=2, enablePrint=True):
    k = k1
    if enablePrint:
        print("K0 = " + str(k))
        print("F(K0) = " + str(F(u, t, k)))
    for _ in range(n):
        k = k - F(u, t, k)/dF(u, t, k)
        if enablePrint:
            print("K" + str(_ + 1) + " = " + str(k))
            print("F(K" + str(_ + 1) + ") = " + str(F(u, t, k)))
    return k 

def secondOrderMethod(du, F, dF, u0, h, interval, enablePrint=True):
    i = interval[0]
    u = u0
    while i < interval[1]-h/2:
        k1 = h*du(u, i)
        k1 = newtonRaphson(k1, F, dF, i, u, enablePrint=enablePrint)
        u = u + k1
        if enablePrint:
            print("u" + str(int(i/h)+1) + " = " + str(u))
        i = i + h
    return u

if __name__ == "__main__":
    def du(u, t):
        return -2*t*(u**2) 
    def F(u, t, k1):
        return k1 + 0.2*(2*t + 0.2)*(u + 0.5*k1)**2
    def dF(u, t, k1):
        return 1 + 0.2*(2*t + 0.2)*(u + 0.5*k1)
    u0 = 1
    h = 0.2
    interval = [0, 0.4]
    secondOrderMethod(du, F, dF, u0, h, interval)
    
