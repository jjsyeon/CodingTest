import sys
input = sys.stdin.readline      

t = int(input())
result = []
for _ in range(t):
    answer = 'YES'
    cnt = int(input())
    nums = sorted([input().strip() for _ in range(cnt)])
    for i in range(cnt-1):
        for j in range(i+1,cnt):
            if nums[i] == nums[j][:len(nums[i])]: 
                answer = 'NO'
                i = j = cnt
                break
            if len(nums[i]) < len(nums[j]): break
    result.append(answer)       

for res in result : print(res)