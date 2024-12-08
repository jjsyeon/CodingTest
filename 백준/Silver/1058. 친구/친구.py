n = int(input())
friends = [list(input()) for _ in range(n)]
relationship = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if relationship[i][j] == 1: continue
        if friends[i][j] == "Y":
            relationship[i][j] = relationship[j][i] = 1
            continue
        for k in range(n):
            if friends[i][k] == "Y" and friends[j][k] == "Y":
                relationship[i][j] = relationship[j][i] = 1
                break

answer = max([sum(lst) for lst in relationship])
print(answer)