def PMpCMc(f, u0, h, interval, order=2, enablePrint=True):
    def P(u, h, u1, u2):
        return u + (h/2)*(3*u1 - u2)
    def M(p1, p2, c):
        return p1 - (5/6)*(p2 - c)
    def C(u, h, m, u_):
        return u + (h/2)*(m + u_)
    u = u0 
    u_ = []
    for j in range(len(u)):
        u_.append(f(interval[0] + j*h, u[j]))
    p = [0]
    for j in range(1, len(u)):
        p.append(P(u[j], h, u_[j], u_[j-1]))
    m = [0]
    c = [0]
    for j in range(1, len(u)):
        m.append(M(p[j], p[j-1], c[j-1])) 
    m_ = []
    for j in range(len(m)):
        m_.append(f(interval[0] + (j+1)*h, m[j]))
    for j in range(1, len(u)):
        c.append(C(u[j], h, m_[j], u_[j]))
    i = interval[0] + h*(order + 1)
    if enablePrint:
            print("u: " + str(u[-1]))
            print("u': " + str(u_[-1]))
            print("p: " + str(p[-1]))
            print("m: " + str(m[-1]))
            print("m': " + str(m_[-1]))
            print("c: " + str(c[-1]))
            print()
    while i < interval[1]+3*h/2:
        u_new = c[-1] + (1/6)*(p[-1] - c[-1])
        u__new = f(i, u_new)
        p_new = P(u[-1], h, u_[-1], u_[-2]) 
        m_new = M(p_new, p[-1], c[-1])
        m__new = f(i, m_new)
        c_new = C(u[-1], h, m__new, u_[-1])
        for j in range(len(u)-1):
            u[j] = u[j+1]
            u_[j] = u_[j+1]
            m[j] = m[j+1]
            m_[j] = m_[j+1]
            p[j] = p[j+1]
            c[j] = c[j+1]
        u[-1] = u_new
        u_[-1] = u__new
        m[-1] = m_new
        m_[-1] = m__new
        p[-1] = p_new
        c[-1] = c_new
        if enablePrint:
            print("u: " + str(u[-1]))
            print("u': " + str(u_[-1]))
            print("p: " + str(p[-1]))
            print("m: " + str(m[-1]))
            print("m': " + str(m_[-1]))
            print("c: " + str(c[-1]))
            print()
        i = i + h
    return u[-1]
    


def PECmE(f, u0, h, interval, m=2, enablePrint=True):
    def P(u, h, u1, u2):
        return u + (h/2)*(3*u1 - u2)
    def C(u, h, u1, u2):
        return u + (h/2)*(u1 + u2)
    u = u0 
    u_ = []
    for j in range(len(u)):
        u_.append(f(interval[0] + j*h, u[j]))
    i = interval[0] + h*len(u)
    k = 0
    while i < interval[1] + h/2:
        if enablePrint:
            for j in range(len(u)):
                print("u" + str(int(i/h) - len(u) + j) + " = " + str(u[j]))
            for j in range(len(u_)):
                print("u'" + str(int(i/h) - len(u) + j) + " = " + str(u_[j]))
        p = P(u[1], h, u_[1], u_[0])
        if enablePrint:
            print("P: " + str(p))
        for _ in range(m):
            if _ == 0:
                e = f((k + 2)*h, p)
            else:
                e = f((k + 2)*h, c)
            c = C(u[1], h, e, u_[1])
            if enablePrint:
                print("E: " + str(e))
                print("C: " + str(c))
        for _ in range(len(u)-1):
            u[_] = u[_+1]
            u_[_] = u_[_+1]
        u[-1] = c
        u_[-1] = f(i, c)
        i = i + h
        k = k + 1
        if enablePrint:
            print()
    return u[-1]

if __name__ == "__main__":
    def f(t, u):
        return -2*t*(u**2) 
    u0 = [1, 0.9615385]
    h = 0.2
    interval = [0, 0.4]
    PMpCMc(f, u0, h, interval)