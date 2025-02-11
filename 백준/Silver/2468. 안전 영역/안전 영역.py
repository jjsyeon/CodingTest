import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
table = [list(map(int,input().split())) for _ in range(n)]

def dfs(x, y, h):
    visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if 0<=mx<n and 0<=my<n and visited[mx][my] == 0 and table[x][y] > h : dfs(mx,my,h)

answer = []
for h in range(101):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and table[x][y] > h : 
                cnt += 1
                dfs(x,y,h)
            else: visited[x][y] = 1
    answer.append(cnt)
    if cnt == 0 : break
    
print(max(answer))