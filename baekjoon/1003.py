T = int(input())
zeros = [1, 0, 1]
ones = [0, 1, 1]

def fibonacci(n):
    if n >= len(zeros):
        for i in range(len(zeros), n+1):
            zeros.append(zeros[i-2] + zeros[i-1])
            ones.append(ones[i-2] + ones[i-1])
    print(zeros[n], ones[n])

for t in range(T):
    num = int(input())
    fibonacci(num)
