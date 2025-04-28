import sys
input = sys.stdin.readline

n, k = map(int, input().split())
height = sorted(list(map(int, input().split())))
sub = [height[i] - height[i-1] for i in range(1,len(height))]

sub.sort()

print(sum(sub[:n - k]) if k > 1 else sum(sub))