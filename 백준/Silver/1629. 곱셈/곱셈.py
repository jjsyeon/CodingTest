import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def dnc(idx):
    if idx == 1 : return A % C
    return ((A if idx%2 else 1) * (dnc(idx//2)**2))% C

print(dnc(B))