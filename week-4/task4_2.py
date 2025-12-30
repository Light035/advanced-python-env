def inside(x, y, R):
    return x*x + y*y < R*R

R = float(input("R: "))

points = []
for name in ["P","F","L"]:
    x = float(input(f"{name}x: "))
    y = float(input(f"{name}y: "))
    points.append((x,y))

count = 0
for p in points:
    if inside(p[0], p[1], R):
        count += 1

print("Inside =", count)
