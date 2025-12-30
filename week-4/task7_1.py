def rect(x, y):
    return x * y

def right_triangle(a, b):
    return 0.5 * a * b

X = float(input("X: "))
Y = float(input("Y: "))
Z = float(input("Z: "))
T = float(input("T: "))

S = right_triangle(X, Y) + right_triangle(Z, T)

print("Area =", S)
