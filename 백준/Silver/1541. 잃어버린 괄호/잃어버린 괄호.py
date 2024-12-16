arr = input().split('-')
answer = int(sum(list(map(int, arr[0].split('+')))))
for item in arr[1:]:
    answer -= sum(list(map(int, item.split('+'))))
print(answer)