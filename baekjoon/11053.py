T = int(input())
items = list(map(int,input().split()))

count = [1 for j in range(T)]
for i in range(T-2,-1,-1):
    temp = []
    for j in range(i+1,T):
        if items[i] < items[j]:
            temp.append(count[j]+1)
    if len(temp) > 0:
        count[i] = max(temp)
    
print(max(count))