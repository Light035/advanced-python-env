eq = input().strip()

a, op, b, _, c = eq

def val(x):
    return int(x) if x != 'x' else None

A, B, C = val(a), val(b), val(c)

if op == '+':
    if A is None:
        print(C - B)
    elif B is None:
        print(C - A)
    else:
        print(A + B)
else:
    if A is None:
        print(C + B)
    elif B is None:
        print(A - C)
    else:
        print(A - B)
