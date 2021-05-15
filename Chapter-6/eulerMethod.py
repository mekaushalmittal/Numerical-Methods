def print_values(u, i):
    print("u"+str(i+1) + " = " + str(u))

def forwardMethod(du, u0, h, interval, enablePrint=True):
    i = interval[0]
    u = u0
    while i < interval[1]:
        u_ = du(u, i)
        u = u + h*u_
        if enablePrint:
            print("u'" + str(int(i/h)) + " = " + str(u_))
            print_values(u, int(i/h))
        i = i + h
    print(i)
    return u

def midPointMethod(du, u0, u1, h, interval, enablePrint=True):
    if enablePrint:
        print_values(u0, -1)
        print_values(u1, 0)
    i = interval[0] + h
    while i < interval[1]-h/2:
        u = u0 + 2*h*du(u1, i)
        if enablePrint:
            print_values(u, int(i/h)-1)
        u0 = u1 
        u1 = u
        i = i + h
    return u

if __name__ == "__main__":
    def du(u, t):
        return t*(u + t) - 2
    u0 = 2
    h = 0.15
    interval = [0, 0.6]
    forwardMethod(du, u0, h, interval)