N, M = map(int, input().split())
cards = list(map(int, input().split()))[:N]
cards.sort(reverse=True)
answer = 0
for a in range(0,N-2):
    if answer > 0 and cards[a] + cards[a+1] + cards[a+2] < answer: break
    for b in range(a+1,N-1):
        if answer > 0 and cards[a] + cards[b] + cards[b+1] < answer: break
        for c in range(b+1,N):
            if cards[a] + cards[b] + cards[c] <= M:
                answer = max(answer, cards[a] + cards[b] + cards[c])
                break
print(answer)