def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Length: "))
A = []

for i in range(m):
    A.append(int(input("Element: ")))

print("Original:", A)

swap(A)

print("Result:", A)
