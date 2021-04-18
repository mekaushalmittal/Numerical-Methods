def calculate_u(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def difference_table(y, n):
    for i in range(1, n):
        for j in range(n - 1, i-1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

def show_table(x, y, n):
    for i in range(n):
        print(x[i], end="\t")
        for j in range(n - i):
            print(y[i][j], end = "\t")
        print("")

if __name__=="__main__":
    n = 5
    x = [ .1, .2, .3, .4, .5 ]
    y = [[0 for i in range(n)] for j in range(n)]
    y[0][0] = 9.9833
    y[1][0] = 4.9667
    y[2][0] = 3.2836
    y[3][0] = 2.4339
    y[4][0] = 1.9177
    value = .25
    sum = y[n-1][0]
    difference_table(y, n)
    show_table(x, y, n)
    u = (value - x[n-1]) / (x[1] - x[0])
    for i in range(1,n):
        sum = sum + (calculate_u(u, i) * y[n-1][i]) / factorial(i)

    print("\nValue at", value, "is", round(sum, 6))
