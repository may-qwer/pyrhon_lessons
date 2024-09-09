def set_maker1():
    e = set(i for i in range(1, 101))
    a1 = set(i for i in e if i%5==2)
    a2 = set(i for i in e if i%5==4)
    a = a1.union(a2)
    b = set(i for i in e if i%7==3)
    c = set(i for i in e if i%3!=1)
    result = a.intersection(b)
    result = result.intersection(c)
    return result

def set_maker2():
    return set(i for i in range(1, 101) if (i%5==2 or i%5==4) and i%7==3 and i%3!=1)

if __name__ == "__main__":
    print(set_maker1())
    print(set_maker2())
