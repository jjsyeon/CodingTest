import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[num for num in arr] for _ in range(2)]

for i in range(1,n):
    dp[0][i] = max(dp[0][i], dp[0][i-1] + dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i])

print(max(max(dp[0]), max(dp[1])))