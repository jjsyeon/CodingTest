T = int(input())

def factorial(num):
    if num < 2: return 1
    value = 1
    for i in range(num): value *= (i+1)
    return value

for test_case in range(T):
    L, R = list(map(int, input().split()))
    print(factorial(R) // (factorial(L) * factorial(R-L)))
