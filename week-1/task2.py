salaries = input().split()
salaries = list(map(int, salaries))
result = max(salaries) - min(salaries)

print(result)
