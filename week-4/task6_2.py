import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
diag = float(input("Diagonal: "))

# разбиваем на два треугольника (по Герону)

def area(x, y, z):
    p = (x+y+z)/2
    return math.sqrt(p*(p-x)*(p-y)*(p-z))

S = area(a,b,diag) + area(c,d,diag)

print("Area =", S)
