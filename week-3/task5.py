import re

n = int(input())
pattern = re.compile(r'^[ABCEHKMOPTXY]\d{3}[ABCEHKMOPTXY]{2}$')

for _ in range(n):
    plate = input().strip()
    if pattern.match(plate):
        print("Yes")
    else:
        print("No")
