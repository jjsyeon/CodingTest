import sys
input = sys.stdin.readline

N = int(input())
request = sorted(list(map(int, input().split())))
amt = int(input())
sum_ = request.copy()
for i in range(1, N): sum_[i] += sum_[i-1]

low, high = 0, N-1
while low < high : 
    mid = (low + high) // 2
    if (sum_[mid] + (N - mid - 1) * request[mid]) <= amt:
        low = mid +1
    else: 
        high = mid
if low == 0 : print(amt // N)
elif low == N-1 and  sum_[low] <= amt: print(request[low])
else : print((amt - sum_[low-1])//(N-low))
