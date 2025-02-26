import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력 처리
N = int(input().strip())
arr = list(map(int, input().strip().split()))

# 누적 합 (Prefix Sum) 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 각 값의 첫 번째와 마지막 등장 위치 저장
first_index = {}
last_index = {}

for i in range(N):
    if arr[i] not in first_index:
        first_index[arr[i]] = i + 1  # 1-based index 저장
    last_index[arr[i]] = i + 1  # 마지막 등장 위치 갱신

# 최대 부분합과 해당 개수 찾기
max_sum = -float('inf')
max_count = 0

for x in first_index:
    start, end = first_index[x], last_index[x]
    sub_sum = prefix_sum[end] - prefix_sum[start - 1]  # 부분합 계산

    if sub_sum > max_sum:
        max_sum = sub_sum
        max_count = 1
    elif sub_sum == max_sum:
        max_count += 1

# 결과 출력
print(max_sum, max_count)