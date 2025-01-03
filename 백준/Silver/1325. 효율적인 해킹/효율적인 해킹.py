import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(s):
    visited = [0] * (n+1)
    visited[s] = 1
    stack = [s]
    while stack:
        curr = stack.pop()
        for c in graph[curr]:
            if not visited[c]:
                visited[c] = 1
                stack.append(c)
    return sum(visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

answer = [dfs(i) for i in range(1, n+1)]
max_ = max(answer)
print(*[i+1 for i in range(n) if answer[i] == max_])