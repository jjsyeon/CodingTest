N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(input())
result = []

for x in range(N-7):
    for y in range(M-7):
        count_case1 = 0
        count_case2 = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        count_case1 += 1
                    if board[i][j] != 'B':
                        count_case2 += 1
                else:
                    if board[i][j] != 'B':
                        count_case1 += 1
                    if board[i][j] != 'W':
                        count_case2 += 1
        result.append(min(count_case1, count_case2))
print(min(result))
