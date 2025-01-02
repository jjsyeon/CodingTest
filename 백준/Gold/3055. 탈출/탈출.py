from collections import deque
import sys
# input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

queue = deque()
visited = [[-1] * c for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*': # 물 차오른 지점 체크
            queue.appendleft((x,y))
        elif graph[x][y] == 'S': # 두더지 시작 지점 체크
            queue.append((x,y))
            visited[x][y] += 1  
            
answer = 'KAKTUS'
while queue and answer == 'KAKTUS':
    x,y = queue.popleft()
    curr_stat = graph[x][y] # 현재 위치의 상태(두더지 있는지, 물이 차올라 있는지)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c : continue # 이동할 위치가 범위 밖이면 넘어가기
        if visited[nx][ny] != -1 : continue # 이동할 위치가 이미 방문한 곳이면 넘어가기
        if graph[nx][ny] == '*' or graph[nx][ny] == 'X': continue # 이동할 위치가 물or돌 이면 넘어가기
        if curr_stat == '*' and graph[nx][ny] == 'D': continue # 다음 위치가 두더지집이면 물 채우면안 됨

        if curr_stat == 'S':
            if graph[nx][ny] == 'D': 
                answer = visited[x][y] + 1
                break
            visited[nx][ny] = visited[x][y] + 1
        
        graph[nx][ny] = curr_stat
        queue.append((nx, ny))

print(answer)