import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]] + [0] * (n-1)

for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))