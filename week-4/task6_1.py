def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("A: "))
b = int(input("B: "))

g = gcd(a, b)
l = a * b // g

print("GCD =", g)
print("LCM =", l)
