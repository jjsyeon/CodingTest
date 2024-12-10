import sys
input = sys.stdin.readline

def binary_search(val, lst):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2 
        if lst[mid] < val : low = mid+1
        elif lst[mid] > val : high = mid-1
        else: return mid
    return -1

def solution(n, c, weights):
    if binary_search(c, weights) != -1 : return 1 # 제품 1개
    low, high = 0, n-1
    while low < high:
        sum_weight = weights[low] + weights[high]
        if sum_weight == c: # 제품 2개
            return 1
        elif sum_weight > c:
            high -= 1
        else: 
            if binary_search(c-sum_weight, weights[low+1:high]) != -1: return 1 # 제품 3개
            low += 1
    return 0

n, c = map(int, input().split())
weights = sorted(list(map(int, input().split())))

print(solution(n,c,weights))