import numpy as np

def print_values(u, i, k1, k2, k3=None, k4=None):
    print("K1 = ", k1)
    print("K2 = ", k2)
    if k3 is not None:
        print("K3 = ", k3)
    if k4 is not None:
        print("K4 = ", k4)
    print("u"+str(i+1) + " = " + str(u))

def secondOrderMethod(f, u0, h, interval, c2=2/3, enablePrint=True):
    i = interval[0]
    u = np.asarray(u0)
    k1 = [0 for i in range((len(u)))]
    k2 = [0 for i in range((len(u)))]
    while i < interval[1]-h/2:
        for j in range(len(u)):
            k1[j] = h*f(i, u)[j]
        k1 = np.asarray(k1)
        for j in range(len(u)):
            k2[j] = h*f(i+c2*h, u+k1)[j]
        k2 = np.asarray(k2)
        u = u + (1/2)*(k1 + k2)
        if enablePrint:
            print_values(u, int(i/h), k1, k2)
        i = i + h
    return u

def fourthOrderMethod(f, u0, h, interval, c2=1/2, enablePrint=True):
    i = interval[0]
    u = np.asarray(u0)
    k1 = [0 for i in range((len(u)))]
    k2 = [0 for i in range((len(u)))]
    k3 = [0 for i in range((len(u)))]
    k4 = [0 for i in range((len(u)))]
    while i < interval[1]-h/2:
        for j in range(len(u)):
            k1[j] = h*f(i, u)[j]
        k1 = np.asarray(k1)
        for j in range(len(u)):
            k2[j] = h*f(i+c2*h, u+k1*c2)[j]
        k2 = np.asarray(k2)
        for j in range(len(u)):
            k3[j] = h*f(i+c2*h, u+k2*c2)[j]
        k3 = np.asarray(k3)
        for j in range(len(u)):
            k4[j] = h*f(i+h, u+k3)[j]
        k4 = np.asarray(k4)
        u = u + (1/6)*(k1 + 2*(k2 + k3) + k4)
        if enablePrint:
            print_values(u, int(i/h), k1, k2, k3, k4)
        i = i + h
    return u

if __name__ == "__main__":
    def f(t, u):
        du = -3*u[0] + 2*u[1]
        dv = 3*u[0] - 4*u[1]
        return [du, dv]
    u0 = np.asarray([0, 0.5])
    interval = [0, 0.4]
    h  = 0.2
    secondOrderMethod(f, u0, h, interval, c2=1)
    fourthOrderMethod(f, u0, h, interval)