numbers = list(map(int, input().split()))
numbers[2] -= numbers[0]
numbers[3] -= numbers[1]
print(min(numbers))
