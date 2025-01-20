from collections import deque

n, m = map(int, input().split())
graph = {i+1:[] for i in range(n)}
for _ in range(m): 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1] * (n+1)
queue = deque([(1,0)])
visited[1] = 0
while queue:
    v, dist = queue.popleft()
    for connected in graph[v]:
        if visited[connected] == -1:
            queue.append((connected, dist+1))
            visited[connected] = dist + 1

max_ = max(visited)
print(visited.index(max_), max_, visited.count(max_))