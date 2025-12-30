import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

def hexagon_area(a):
    return 6 * triangle_area(a)

a = float(input("Side length: "))
print("Hexagon area =", hexagon_area(a))
