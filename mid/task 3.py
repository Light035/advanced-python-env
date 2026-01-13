if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    t = tuple(numbers)
    print(hash(t))

