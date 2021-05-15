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

def lagrangianInterpolation(x_arr, fx, x, enable_print=True):
    out = 0
    for i in range(len(x_arr)):
        out += (li(x_arr, i, x, enable_print=enable_print)*fx[i])
    return out 

if  __name__ == "__main__":
    x_arr = [0, 1, 2, 4, 5, 6]
    fx = [1, 14, 15, 5, 6, 19]
    x = 3
    print("f(" + str(x) + "): ", lagrangianInterpolation(x_arr, fx, x))