import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y) -> int:
        point = 0
        if x < 0 or y < 0 or x >= len(maps) or y >= len(maps[0]):
            return point
        if maps[x][y] != 'X' and visited[x][y] == 0:
            visited[x][y] = 1
            for i in range(4):
                point += dfs(x + dx[i], y + dy[i])
            return int(maps[x][y]) + point
        return point

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] != "X" and visited[x][y] == 0 :
                answer.append(dfs(x, y))         
    
    if len(answer) == 0 : return [-1]
    return sorted(answer)