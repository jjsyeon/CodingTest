import sys
input = sys.stdin.readline

W, H, K = map(int, input().split())
N = int(input())
x_cut = [0] + list(map(int, input().split())) + [H]
M = int(input())
y_cut = [0] + list(map(int, input().split())) + [W]

xs = sorted([x_cut[i+1] - x_cut[i] for i in range(N+1)])
ys = sorted([y_cut[i+1] - y_cut[i] for i in range(M+1)])

cnt = 0

def binary_search(s, e, val):
    while s < e:
        mid = (s+e) // 2 
        if val >= ys[mid] : s = mid+1
        else: e = mid

    return s

for x in xs:
    if x > K : break
    val = K // x
    cnt += binary_search(0, M+1, val)

print(cnt)