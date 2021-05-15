def li(x_arr, i, x, enable_print=True):
    out = 1
    for _ in range(len(x_arr)):
        if _ == i:
            continue
        else:
            out *= ((x - x_arr[_])/(x_arr[i] - x_arr[_]))
    if enable_print:
        print("l" + str(i) + ": " + str(out))
    return out 

def lagrangianDifferentiation(x_arr, fx, x, enable_print=True):
    out = 0
    for i in range(len(x_arr)):
        out += (li(x_arr, i, x, enable_print=enable_print)*fx[i])
    return out 

if  __name__ == "__main__":
    x_arr = [6., 6.1, 6.2, 6.3, 6.4]
    fx = [.1750, -.1998, -0.2223, -.2422, -.2596]
    x = 6.3
    print(lagrangianDifferentiation(x_arr, fx, x))