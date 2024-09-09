from heapq import heappush, heappop

def solution(n, works):
    remain = sum(works) - n
    if remain <= 0 : return 0

    works = sorted([-w for w in works])

    for t in range(n):
        max_w = heappop(works)
        heappush(works, max_w+1)
    
    return sum([w**2 for w in works])