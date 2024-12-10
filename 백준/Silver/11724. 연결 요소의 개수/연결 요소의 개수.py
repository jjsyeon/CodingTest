import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u, graph, visited):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)

n, m = map(int, input().split()) 
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0 
visited = [0] * (n+1)
for u in range(1, n+1):
    if not visited[u]:
        dfs(u, graph, visited)
        answer += 1 
        
print(answer)