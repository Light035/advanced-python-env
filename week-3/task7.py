from collections import Counter

items = input().split()
cnt = Counter(items)

print("Purchase frequency:")
for k, v in cnt.items():
    print(f"{k}: {v}")

most = max(cnt, key=cnt.get)
print(f"Most popular item: {most}")

once = [k for k, v in cnt.items() if v == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for k, v in cnt.most_common():
    print(k, v)
