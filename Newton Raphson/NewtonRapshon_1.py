# Implementation of Newton-Raphson method for the example given in the book
# To perform four iterations of the Newton-Raphson method to find the smallest positive root of the equation f(x) = x^3 - 5x + 1 = 0 

def function(x):
    val = pow(x, 3) - 5*x + 1
    return val 

def derivative(x):
    val = 3*pow(x, 2) - 5
    return val 

def newton_raphson(x_k):
    div = function(x_k)/derivative(x_k)
    x_k_1 = x_k - div
    x_k_1 = round(x_k_1, 6)
    return x_k_1

x_0 = 0.5
for i in range(4):
    x_i = newton_raphson(x_0)
    print("x_" + str(i+1) + " = " + str(x_i))
    x_0 = x_i
    i+=1

print()
print("The exact value correct to six decimal places is ", x_i)

# Submitted by Sarthak Khoche (IMT2017038)