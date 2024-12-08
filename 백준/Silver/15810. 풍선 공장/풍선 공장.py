import sys
input = sys.stdin.readline

n, m = map(int, input().split())
capacity = list(map(int, input().split()))

min_t, max_t = 1, min(capacity) * m
done = 0
while min_t <= max_t:
    t = (min_t + max_t) // 2
    done = sum([t//cap for cap in capacity])
    if done >= m : max_t = t-1
    else : min_t = t+1

print(min_t)