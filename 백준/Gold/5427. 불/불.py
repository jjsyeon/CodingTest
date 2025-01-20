from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1] 

for t in range(T):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]

    queue = deque()
    for x in range(h):
        for y in range(w):
            if building[x][y] == '@':
                queue.append([building[x][y], x, y, 0])
            elif building[x][y] == '*':
                queue.appendleft([building[x][y], x, y, 0])

    answer = 'IMPOSSIBLE'
    while queue and answer == 'IMPOSSIBLE':
        item, x, y, time = queue.popleft()
        if item == '@' and (x == 0 or x == h-1 or y == 0 or y == w-1):
            answer = time + 1
            break
        else:
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if  mx < 0 or mx >= h or my < 0 or my >= w: continue
                elif building[mx][my] == '#' or building[mx][my] == '*' or building[mx][my] == item: continue
                building[mx][my] = item
                queue.append([building[mx][my], mx, my, time+1])

    print(answer)