a = input()
dot = a.find(".")

integer = a[:dot]
fractional = a[dot + 1:]

print(fractional + "." + integer)

