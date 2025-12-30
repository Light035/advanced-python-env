def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

num = A*D - C*B
den = B*D

g = gcd(abs(num), den)

print(f"{num//g}/{den//g}")
