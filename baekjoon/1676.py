from math import factorial
numbers = int(input())
count = 0
for number in str(factorial(numbers))[::-1]:
    if number != '0':
        break
    count += 1
print(count)
