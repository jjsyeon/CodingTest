n = int(input())

if n % 2 == 1: print(0)
else:
    dp = [1]
    for i in range(1, n//2+1):
        dp.append(dp[i-1] + sum(dp)*2) 
    print(dp[-1])