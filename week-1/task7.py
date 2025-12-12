a = float(input("First number: "))
op = input("Operation: ")
b = float(input("Second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: division by zero")
else:
    print("Invalid operation")
