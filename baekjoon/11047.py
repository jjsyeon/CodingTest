N, K= map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

result = 0

for i in range(N):
    if K == 0:
        break
    result += K // coins[N-1-i]
    K %= coins[N-1-i]

print(result)