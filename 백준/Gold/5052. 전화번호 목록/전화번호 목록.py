import sys
input = sys.stdin.readline      

t = int(input())
result = []
for _ in range(t):
    answer = 'YES'
    cnt = int(input())
    nums = sorted([input().strip() for _ in range(cnt)])
    for i in range(cnt-1):
        if nums[i] == nums[i+1][:len(nums[i])]: 
            answer = 'NO'
            i = j = cnt
            break
    result.append(answer)       

for res in result : print(res)