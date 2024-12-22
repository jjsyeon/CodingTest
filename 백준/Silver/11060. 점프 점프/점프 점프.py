n = int(input())
arr = list(map(int, input().split()))
dp = [0] + [n] * (n-1)

for i in range(n):
    for j in range(1, arr[i]+1):
        if 0 <= i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
            
print(dp[-1] if dp[-1] != n else -1)