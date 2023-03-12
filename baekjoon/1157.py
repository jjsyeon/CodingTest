s = list(input().upper())
alphabets = list(set(s))
times = -1
max_index = -1
count = 0
for times in range(len(alphabets)):
    if s.count(alphabets[times]) > count:
        count = s.count(alphabets[times])
        max_index = times
    elif s.count(alphabets[times]) == count:
        print('?')
        times = 0
        break

if times == len(alphabets) - 1: print(alphabets[max_index])
