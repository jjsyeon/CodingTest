# s = list(input().upper())
# alphabets = list(set(s))
# times = -1
# max_index = -1
# count = 0
# for times in range(len(alphabets)):
#     if s.count(alphabets[times]) > count:
#         count = s.count(alphabets[times])
#         max_index = times
#     elif s.count(alphabets[times]) == count:
#         print('?')
#         times = 0
#         break

# if times == len(alphabets) - 1: print(alphabets[max_index])

# 위에 틀림 : 틀린 이유 리뷰

s = list(input().upper())
alphabets = list(set(s))
times = -1
max_index = -1
cnt_list = []
for times in range(len(alphabets)):
    cnt = s.count(alphabets[times])
    cnt_list.append(cnt)
    max_index = times

if cnt_list.count(max(cnt_list)) == 1:
    print(alphabets[cnt_list.index(max(cnt_list))])
else: print('?')
