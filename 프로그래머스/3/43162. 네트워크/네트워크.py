def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(i):
        visited[i] = 1 
        for c, connection in enumerate(computers[i]):
            if connection and visited[c] == 0: dfs(c)
    
    for i in range(n):
        if visited[i]: continue
        dfs(i)
        answer += 1 

    return answer