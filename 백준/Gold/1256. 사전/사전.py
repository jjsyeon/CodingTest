n, m, k = map(int, input().split())
dp = [[1] * (m+1) for _ in range(n+1)] # a만 있거나 z만 있거나 a또는 z가 1인 경우의 값이 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if k > dp[n][m]: print(-1)
else: 
    answer = ''
    while k and n and m:
        if n == 0 or m == 0: break
        if k <= dp[n-1][m]: # a로 시작하면서 뒤에 a (n-1)개 z (m)개를 나열하는 게 적절한 경우
            answer += 'a'
            n -= 1
        else: # z로 시작하면서 뒤에 a (n)개 z (m-1)개를 나열하는 게 적절한 경우
            answer += 'z'
            k -= dp[n-1][m] # z로 시작하는 단어로 설정해서 a로 시작하는 단어의 경우의 수 모두 건너뛰기
            m -= 1
    answer += 'a' * n + 'z' * m
    print(answer)