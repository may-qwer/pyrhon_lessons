import math
#
# #function for calculate exp(x)
# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
#
# def fact_2(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact_2(n-1)
#
# def calculation_expx(x, n):
#     expx = 1
#     for i in range(1, n+1):
#         expx += (x**i)/(fact(i))
# #        print(i, expx)
#     return expx
#
# def calculation_expx_2(x, n):
#     expx = 1
#     for i in range(1, n+1):
#         expx += (x**i)/(fact_2(i))
#     return expx
#
# print(calculation_expx(1, 500))
# print(calculation_expx_2(1, 500))
# print(math.exp(1))

# def solve_eqn(f, x0, n):
#     x = x0
#     for k in range(1, n+1):
#         x = f(x)
#     return x
#
# def eqn_1(x):
#     return (x**2+5)/8
#
# print(solve_eqn(eqn_1, 1, 600))

def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)

for i in range(1, 16):
    print(Fib(i), end = " ")

def solve_fi(n):
    return (Fib(n))/(Fib(n-1))

print("")
print (solve_fi(30))
print((1 + 5**0.5)/2)
