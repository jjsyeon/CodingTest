T = int(input())
numbers = list(map(int, input().split()))
answer = T
for test_case in range(T):
    number = numbers[test_case]

    for i in range(2, number+1):
        if number % i == 0:
            break
        if i == number:
            answer+=1
    

print(answer)
