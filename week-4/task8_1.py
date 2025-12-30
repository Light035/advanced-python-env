n = int(input("n: "))

for x in range(1, n+1):
    s = str(x)
    ok = True
    for d in s:
        if d == '0' or x % int(d) != 0:
            ok = False
            break
    if ok:
        print(x)
