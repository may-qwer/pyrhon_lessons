import math

def F(g):
    return lambda x: g(x)

@F
def g(f):
    return lambda x: math.exp(f(x))

@F
@g
def f(x):
    return x

if __name__ == "__main__":
    for i in range(10):
        print(f(i))