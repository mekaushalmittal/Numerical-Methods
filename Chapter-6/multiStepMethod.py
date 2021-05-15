adamsBashforth = [[1, 3/2, 23/12, 55/24, 1901/720], 
                  [None, -1/2, -16/12, -59/24, -2774/720],
                  [None, None, 5/12, 37/24, 2616/720],
                  [None, None, None, -9/24, -1274/720],
                  [None, None, None, None, 251/720]]
nystrom = [[2, 2, 7/3, 8/3, 269/90], 
          [None, 0, -2/3, -5/3, -266/90],
          [None, None, 1/3, 4/3, 294/90],
          [None, None, None, -1/3, -146/90],
          [None, None, None, None, 29/90]]

def print_values(u, f_arr, i):
    for j in range(len(u)):
        print("u" + str(i + j) + " = " + str(u[j]))
    for j in range(len(f_arr)):
        print("f" + str(i + j) + " = " + str(f_arr[j]))
    print()

def multiStepMethod(f, u0, h, interval, order=2, method_type=0, enablePrint=True):
    '''
    method_type:
    0 :: Adam-Bashforth Method
    1 :: Nystrom Method
    '''
    if method_type == 0:
        gamma = adamsBashforth
    else:
        gamma = nystrom
    u = u0
    f_arr = []
    for j in range(order):
        f_arr.append(f(interval[0] + j*h, u[j]))
    i = interval[0] + order*h
    while i < interval[1]+h/2:
        if enablePrint:
            print_values(u, f_arr, int(i/h)-order)
        u_ = u[-1]
        for j in range(order):
            u_ += h*f_arr[-(j + 1)]*gamma[j][order-1]
        for j in range(order - 1):
            u[j] = u[j+1] 
            f_arr[j] = f_arr[j+1]
        u[-1] = u_ 
        f_arr[-1] = f(i, u_)
        i = i + h
    return u[-1]

if __name__ == "__main__":
    def f(t, u):
        return t - u*u
    u0 = [1, 0.9097777777777778]
    h = 0.1
    interval = [.1, .3]
    multiStepMethod(f, u0, h, interval)