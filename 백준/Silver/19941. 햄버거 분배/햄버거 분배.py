import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = input()
visited = [0 if item == "H" else 1 for item in arr]
answer = 0

for i in range(len(arr)):
    if arr[i] == "P":
        start = i-k if i-k>=0 else 0
        end = i+k+1 if i+k+1<=len(arr) else len(arr)
        candidates = visited[start:end]
        if 0 in candidates:
            idx = candidates.index(0) + start
            visited[idx] = 1
            answer += 1

print(answer)