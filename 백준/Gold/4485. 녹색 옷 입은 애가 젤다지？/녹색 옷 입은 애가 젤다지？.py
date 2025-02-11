import sys
from math import inf
import heapq
input = sys.stdin.readline

t = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while (n := int(input())): 
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[inf] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    visited[0][0] = graph[0][0]
    while heap:
        coin, x, y = heapq.heappop(heap)
        if visited[x][y] < coin : continue     
        for i in range(4):
            mx, my = x+dx[i], y+ dy[i]
            # dst = coin + graph[mx][my]
            if 0<=mx<n and 0<=my<n and visited[mx][my] > coin + graph[mx][my]: 
                heapq.heappush(heap, (coin + graph[mx][my], mx, my))
                visited[mx][my] = coin + graph[mx][my]
            if mx == n-1 and my == n-1: break
    print(f"Problem {t}: {visited[-1][-1]}")
    t+=1
