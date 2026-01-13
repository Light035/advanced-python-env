a = input()
b = input()

m = len(b)
rotations = set()

bb = b + b
for i in range(len(b)):
    rotations.add(bb[i:i+m])

ans = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in rotations:
        ans += 1

print(ans)
