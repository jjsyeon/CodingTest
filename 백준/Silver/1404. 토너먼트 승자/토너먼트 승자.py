arr = list(map(int, input().split()))
prob = [[0] * 8 for _ in range(8)]
idx = 0
for i in range(8):
    for j in range(i+1, 8):
        prob[i][j] = arr[idx] / 100.0 
        prob[j][i] = 1 - prob[i][j]
        idx += 1

cases = [1] * 8 # 참가자가 어떤 라운드에 도달할 수 있는 확률을 저장하는 list
for level in range(1,4):
    group = 2**level
    new_cases = [0] * 8
    for i in range(8):
        for j in range((i//group)*group, (i//group)*group + group):
            new_cases[i] += cases[i] * cases[j] * prob[i][j]
            prob[i][j] = 0
    cases = new_cases[:]

for p in cases:
    print(f'{p:.10f}', end=" ")