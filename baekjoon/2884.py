H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    M = 15 + M
    H = (H - 1) % 24

print(H, M)
