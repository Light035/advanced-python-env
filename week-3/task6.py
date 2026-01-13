lst = input().split()

def all_eq(lst):
    max_len = max(len(s) for s in lst)
    return [s + "_" * (max_len - len(s)) for s in lst]

print(all_eq(lst))