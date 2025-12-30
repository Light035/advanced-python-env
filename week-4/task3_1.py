import math

def hyp(a, b):
    return math.sqrt(a*a + b*b)

a1 = float(input("Triangle1 side1: "))
b1 = float(input("Triangle1 side2: "))
a2 = float(input("Triangle2 side1: "))
b2 = float(input("Triangle2 side2: "))

h1 = hyp(a1, b1)
h2 = hyp(a2, b2)

print("Hyp1 =", h1)
print("Hyp2 =", h2)

if h1 > h2:
    print("First is bigger")
elif h2 > h1:
    print("Second is bigger")
else:
    print("Equal")
