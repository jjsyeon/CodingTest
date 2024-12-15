import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    start, end = 0, m
    bef_item = -1
    answer = []
    for item in a:
        if item == bef_item:
            answer.append(answer[-1])
        else:
            for i in range(start,end):
                if item > b[i]:
                    answer.append(end-i)
                    break
            else: break
            start = i
    print(sum(answer))