import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
graph = dict()
for _ in range(n):
    x, y = map(int, input().split())
    graph[x] = y

sorted_keys = sorted(graph.keys())

q = int(input())
for _ in range(q):
    x = float(input())
    min_x, max_x = sorted_keys[bisect_left(sorted_keys, x)-1], sorted_keys[bisect_left(sorted_keys, x)]
    if graph[min_x] > graph[max_x]: print(-1)
    elif graph[min_x] < graph[max_x]: print(1)
    else: print(0)