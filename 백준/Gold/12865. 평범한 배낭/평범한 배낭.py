import sys
input = sys.stdin.readline

n, k = map(int,input().split())
baggage = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for b in range(1,n+1):
    weight, value = baggage[b]
    for d in range(1,k+1): 
        if d >= weight:
            dp[b][d] = max(dp[b-1][d], value + dp[b-1][d-weight])
        else: 
            dp[b][d] = dp[b-1][d]

print(dp[-1][-1])