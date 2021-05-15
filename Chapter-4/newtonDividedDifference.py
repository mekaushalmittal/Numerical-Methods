import numpy as np 

def getDividedDifference(x0, g):
    temp = [g]
    for i in range(len(g)-1):
        temp_2 = [(temp[-1][j+1]-temp[-1][j])/(x0[i+j+1]-x0[j]) for j in range(len(g)-(i+1))]
        temp.append(temp_2)
    return [each[0] for each in temp]

def newtonDividedDifference(x0, g, x):
    f0_arr = getDividedDifference(x0, g)
    out = 0
    for i in range(0, len(f0_arr)):
        sum_ = 1
        for j in range(i):
            sum_*= x-j
        out += f0_arr[i]*sum_
    return out 

if __name__ == "__main__":
    x0 = [0, 1, 2, 4, 5, 6]
    g = [1, 14, 15, 5, 6, 19]
    x = 3
    fx = newtonDividedDifference(x0, g, x)
    fn_arr = getDividedDifference(x0, g)
    print("Given x: ", x0)
    print("Given f(x): ", g)
    print("Given x at which to evaluate: ", x)
    print("Divided differences: ")
    for i in range(len(fn_arr)):
        print("\t(▽^"+str(i)+")fn: ", fn_arr[i]) 
    print("Obtained f(x): ", fx)