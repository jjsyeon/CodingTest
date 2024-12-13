import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = dict()
for _ in range(n):
    inputs = list(map(int, input().split()))
    medals[inputs[0]] = inputs[1:]

answer = 1
for country in medals.keys():
    if country == k: continue
    for i in range(3):
        # print(answer)
        if medals[k][i] < medals[country][i] :
            answer += 1
            break
        elif medals[k][i] > medals[country][i] :
            break
        
print(answer)