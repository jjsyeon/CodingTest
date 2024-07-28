from collections import deque
def solution(board):
    # 초기화
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    maxX, maxY = len(board), len(board[0])
    visited = [list(0 for _ in range(maxY)) for _ in range(maxX)]
    for idx, row in enumerate(board):
        if "R" in row: 
            start = [idx, row.find("R"), answer]
            break
    
    # 움직이는 함수 정의
    def move(x,y,direction):
        while True:
            x += dx[direction]
            y += dy[direction]
            if x<0 or x>=maxX or y<0 or y>=maxY:break
            if board[x][y]=="D": break
        x -= dx[direction]
        y -= dy[direction]
        return x, y
    
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    while queue:
        x, y, answer = queue.pop()
        # visited[x][y] = 1
        for direction in range(4):
            temp_x, temp_y = move(x,y,direction)
            if board[temp_x][temp_y] == "G":
                return answer + 1
            if visited[temp_x][temp_y] == 1: continue
            visited[temp_x][temp_y] = 1
            queue.appendleft([temp_x, temp_y, answer+1])
    return -1