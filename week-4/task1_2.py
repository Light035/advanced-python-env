def process_array(arr):
    total = sum(arr)
    avg = total / len(arr)
    return total, avg


arrays = []
for i in range(1, 4):
    print(f"Array {i}:")
    n = int(input("Enter size (<=15): "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))
    arrays.append(arr)

for i, arr in enumerate(arrays, start=1):
    total, avg = process_array(arr)
    print(f"Array {i}: sum = {total}, average = {avg}")
