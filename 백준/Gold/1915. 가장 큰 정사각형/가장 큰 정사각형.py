
n, m = map(int, input().split())
table = [[0] * (m+1)] + [[0] + [int(item) for item in list(input())] for _ in range(n)]
answer = 0

for r in range(1, n+1):
    for c in range(1,m+1):
        if table[r][c] != 0:
            table[r][c] += min(table[r-1][c-1], table[r-1][c], table[r][c-1])
        if table[r][c] > answer : answer = table[r][c]

print(answer**2)