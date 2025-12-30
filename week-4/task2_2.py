def rectangle_area(a, b):
    return a * b

for i in range(3):
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    print("Area =", rectangle_area(a, b))
