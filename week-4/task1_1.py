import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

def square_area(a):
    return a * a


print("Choose shape:\n1 - Circle\n2 - Rectangle\n3 - Triangle\n4 - Square")
choice = int(input("Enter number: "))

if choice == 1:
    r = float(input("Radius: "))
    print("Area =", circle_area(r))

elif choice == 2:
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    print("Area =", rectangle_area(a, b))

elif choice == 3:
    a = float(input("Base: "))
    h = float(input("Height: "))
    print("Area =", triangle_area(a, h))

elif choice == 4:
    a = float(input("Side: "))
    print("Area =", square_area(a))

else:
    print("Invalid choice")
