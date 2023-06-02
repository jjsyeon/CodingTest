Node = int(input())
relation = int((input()))
rel_dict = {(i+1):set() for i in range(Node)}
for i in range(relation):
    x, y = map(int, input().split())
    rel_dict[x].add(y)
    rel_dict[y].add(x)

cnt = 0
visited = [0] * (Node+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in rel_dict[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
dfs(1)
print(cnt)
