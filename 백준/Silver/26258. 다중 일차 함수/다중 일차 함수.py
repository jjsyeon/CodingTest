import sys
input = sys.stdin.readline

def binary_search(target):
    min_x, max_x = 0, len(graph)-1
    while max_x - min_x > 1:
        mid_x = (min_x + max_x) // 2
        if graph[mid_x][0] < target : min_x = mid_x
        elif graph[mid_x][0] > target : max_x = mid_x
    return min_x, max_x

n = int(input())
graph = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : x[0])

q = int(input())
for _ in range(q):
    x = float(input())
    min_x, max_x = binary_search(x)
    if graph[min_x][1] > graph[max_x][1]: print(-1)
    elif graph[min_x][1] < graph[max_x][1]: print(1)
    else: print(0)