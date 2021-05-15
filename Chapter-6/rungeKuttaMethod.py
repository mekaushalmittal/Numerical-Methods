def print_values(u, i, k1, k2, k3=None, k4=None):
    print("K1 = ", k1)
    print("K2 = ", k2)
    if k3:
        print("K3 = ", k3)
    if k4:
        print("K4 = ", k4)
    print("u"+str(i+1) + " = " + str(u),"\n")


def secondOrderMethod(du, u0, h, interval, c2=2/3, modifiedEuler=False, enablePrint=True):
    if modifiedEuler:
        c2 = 1/2
    i = interval[0]
    u = u0
    while i < interval[1]-h/2:
        k1 = h*du(u, i)
        k2 = h*du(u+c2*k1, i+c2*h)
        if modifiedEuler:
            u = u + k2
        else:
            u = u + (1/2)*(k1+k2)
        if enablePrint:
            print_values(u, int(i/h), k1, k2)
        i = i + h
    return u

def thirdOrderMethod(du, u0, h, interval, c2=2/3, enablePrint=True):
    i = interval[0]
    u = u0
    while i < interval[1]-h/2:
        k1 = h*du(u, i)
        k2 = h*du(u+c2*k1, i+c2*h)
        k3 = h*du(u+c2*k2, i+c2*h)
        u = u + (1/8)*(2*k1+3*(k2 + k3))
        if enablePrint:
            print_values(u, int(i/h), k1, k2, k3)
        i = i + h
    return u

def fourthOrderMethod(du, u0, h, interval, c2=1/2, enablePrint=True):
    i = interval[0]
    u = u0
    while i < interval[1]+h/2:
        k1 = h*du(u, i)
        k2 = h*du(u+c2*k1, i+c2*h)
        k3 = h*du(u+c2*k2, i+c2*h)
        k4 = h*du(u+k3, i+h)
        if enablePrint:
            print("du(u, i) = ", du(u, i))
            print("du(u+c2*k1, i+c2*h) = ", du(u+c2*k1, i+c2*h))
            print("du(u+c2*k2, i+c2*h) = ", du(u+c2*k2, i+c2*h))
            print("du(u+k3, i+h) = ", du(u+k3, i+h))
            print_values(u, int(i/h), k1, k2, k3, k4)
        u = u + (1/6)*(k1+2*(k2 + k3)+k4)
        i = i + h
    return u

if __name__ == "__main__":
    def du(u, t):
        return (u + t)**(0.5)
    u0 = 0.41
    h = 0.2
    interval = [0.4, 0.8]
    # secondOrderMethod(du, u0, h, interval)
    # thirdOrderMethod(du, u0, h, interval)
    fourthOrderMethod(du, u0, h, interval)
