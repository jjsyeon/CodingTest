import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited[start] = 1
    queue = deque([(start, 0)])
    while queue:
        v, dst = queue.popleft()
        for item in graph[v]:
            i, l = item
            if not visited[i] and l != 0:
                if i == end:
                    return dst + l
                queue.append((i, dst + l))
                visited[i] = 1
    return 0

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, distance = map(int, input().split())
    graph[x].append((y, distance))
    graph[y].append((x, distance))

for _ in range(m):
    x, y = map(int, input().split())
    visited = [0] * (n+1)
    print(bfs(x,y))