from collections import deque

def bfs(graph, start):
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

N, M = map(int,input().split())
relation = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    relation[i].append(j)
    relation[j].append(i)

result = []
for i in range(1, N+1):
    result.append(bfs(relation, i))
print(result.index(min(result))+1)
