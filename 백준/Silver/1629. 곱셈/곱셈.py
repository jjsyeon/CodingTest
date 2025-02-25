import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def dnc(idx):
    if idx == 1 : return A % C
    if idx % 2:
        return (A * dnc(idx//2)**2) % C
    else:
        return (dnc(idx//2)**2)%C

print(dnc(B))