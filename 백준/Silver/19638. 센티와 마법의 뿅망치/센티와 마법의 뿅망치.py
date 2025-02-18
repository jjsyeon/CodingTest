import sys
import heapq
input = sys.stdin.readline

n, h, t = map(int, input().split())
giants =[-int(input()) for _ in range(n)]
heapq.heapify(giants)

for attack in range(t):
    g = -heapq.heappop(giants)
    if h > g:
        print(f"YES\n{attack}")
        break
    elif g == 1: 
        print("NO\n1" if h == 1 else "YES\n{attack}")
        break
    heapq.heappush(giants, -(g//2))
else:
    biggest = -heapq.heappop(giants)
    print(f"NO\n{biggest}" if biggest >= h else f"YES\n{attack+1}")
