import sys
import heapq
input = sys.stdin.readline

def sol():
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    size, time, eat_amount = 2, 0, 0
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9 : shark = (i,j); space[i][j] = 0; break

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]  
    def get_next_item(shark):
        sx, sy = shark
        visited = [[0] * n for _ in range(n)]
        visited[sx][sy] = 1
        queue = []
        heapq.heappush(queue, (21*sx+sy, sx, sy, 0))
        while queue:
            _, x, y, dst = heapq.heappop(queue)
            if 0 < space[x][y] < size: return x,y,dst
            for i in range(4):
                mx, my = x+dx[i], y+dy[i]
                if 0<=mx<n and 0<=my<n and visited[mx][my] == 0:
                    if space[mx][my] > size : continue
                    visited[mx][my] = 1
                    heapq.heappush(queue, ((dst+1)*500 + 21*mx+my, mx, my, dst+1))
        return

    while (next_ := get_next_item(shark)):
        time += next_[2]
        shark = (next_[0], next_[1])
        space[next_[0]][next_[1]] = 0
        eat_amount += 1
        if eat_amount == size:
            size+=1
            eat_amount=0
        
    print(time)

sol()