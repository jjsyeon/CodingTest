T = int(input())
answer = ""
size_list = []
for test_case in range(T):
    size = list(map(int, input().split()))
    size_list.append(size)

for test_case in range(T):
    rank = 1
    for i in range(T):
        if i == test_case: continue
        if size_list[i][0] > size_list[test_case][0] and size_list[i][1] > size_list[test_case][1]:
            rank += 1
    answer += str(rank) + ' '

print(answer)