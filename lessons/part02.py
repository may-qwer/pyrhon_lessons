n = 1e6+1
while True:
    dz = 1/n
    dotin = 0
    i = 0
    while i <= n:
        x = dz * i
        j = 0
        while j <=n:
            y = dz * j
            if y <= x and y >= x**2:
                dotin += 1
            j += 1
        i += 1
    s = dotin/((n+1)**2)
    n += 500
    if n > 1e6:
        break
    print("N = " ,n ,"S = ",s)
