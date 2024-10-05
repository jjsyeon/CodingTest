def solution(m, n, puddles):
    distance = [[0 if [j,i] not in puddles else -1 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i*j == 1 : distance[i][j] = 1
            elif distance[i][j] != -1:
                distance[i][j] = distance[i-1][j] + distance[i][j-1]
            else:
                distance[i][j] = 0

    return distance[-1][-1] % 1000000007