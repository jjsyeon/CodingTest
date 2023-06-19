N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    length = (start + end) // 2
    remain=0
    for t in tree:
        if t >= length: remain += t-length
    # if remain == M: break
    if remain >= M: start = length + 1
    else: end = length - 1

print(end)
