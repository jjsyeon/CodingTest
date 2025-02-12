import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    graph = {i : [] for i in range(1, n+1)}
    for _ in range(n-1):
        p, c = map(int, input().split())
        graph[c].append(p)

    x, y = map(int, input().split())
    x_parents = [x]
    y_parents = [y]
    while ((p := graph[x_parents[-1]]) != []): x_parents.append(p[0])
    while ((p := graph[y_parents[-1]]) != []): y_parents.append(p[0])
    for p in x_parents:
        if p in y_parents: 
            print(p)
            break