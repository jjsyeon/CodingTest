import sys
input = sys.stdin.readline

t = int(input())
case = [int(input()) for _ in range(t)]
dp = [1, 1, 2] 
for i in range(3, max(case)+1): dp.append(sum(dp[i-3:i])%1000000009)
print("\n".join([str(dp[c]) for c in case]))