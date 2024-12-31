n = int(input())
m = int(input())
arr = [0] + list(map(int,input().split())) + [n]

height = []
for i in range(1, m+2):
    if i == 1 or i == (m+1):
        h = arr[i] - arr[i-1]
    else:
        h =  (arr[i] - arr[i-1] + 1) // 2
    height.append(h)
        
print(max(height))