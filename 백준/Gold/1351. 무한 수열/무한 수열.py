import sys
from collections import defaultdict
input = sys.stdin.readline

N, P, Q = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

def get_val(idx):
    if not dp[idx] : dp[idx] = get_val(idx//P) + get_val(idx//Q)
    return dp[idx]

print(get_val(N))