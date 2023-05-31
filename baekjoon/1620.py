import sys

input = sys.stdin.readline # 해당 라인 없으면 시간 초과

N, M = map(int, input().split())
pocket_lst = {}
for i in range(1,N+1):
    value = input().rstrip()
    pocket_lst[i] = value
    pocket_lst[value] = i 
    
for m in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pocket_lst[int(q)])
    else:
        print(pocket_lst[q])
