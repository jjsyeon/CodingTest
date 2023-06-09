from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
visited_bfs = [0] * (N + 1)
visited_dfs = [0] * (N + 1)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_bfs[i] = 1

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)
dfs(V)
print()
bfs(V)
