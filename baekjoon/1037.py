N = int(input())
numbers = sorted(list(map(int,input().split())))

length = len(numbers)
if length % 2 == 0:
    print(numbers[length//2 - 1] * numbers[length//2])
else:
    print(numbers[length//2] * numbers[length//2])

# or

N = int(input())
numbers = sorted(list(map(int,input().split())))

print(numbers[0] * numbers[-1])
