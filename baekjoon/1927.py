import sys
from heapq import heappush, heappop
input = sys.stdin.readline
T = int(input())
heap = []
for i in range(T):
    num = int(input())
    if num > 0:
        heappush(heap, num)
    elif num == 0: 
        if len(heap) == 0: print(0)
        else: print(heappop(heap))
