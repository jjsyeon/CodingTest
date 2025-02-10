import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph  = {i:[] for i in range(1,n+1)}
for _ in range(n-1): 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (n+1)

def bfs(s):
    visited[s] = 1
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for c in graph[v]:
            if not visited[c] :
                visited[c] = v
                queue.append(c)

bfs(1)
print("\n".join(map(str, visited[2:])))