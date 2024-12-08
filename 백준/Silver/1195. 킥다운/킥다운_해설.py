short_part = input()
long_part = input()

if len(short_part) > len(long_part): #짧은 배열, 긴 배열 맞춰주기
    short_part, long_part = long_part, short_part

do_more = 1
# 옆으로 안 삐져나오는 경우
length = len(long_part)
for i in range(length - len(short_part) + 1):
    for j in range(length - len(long_part) + 1):
        tmp_short = "0"*i + short_part + "0"*(length-len(short_part)-i)
        tmp_long = "0"*j + long_part + "0"*(length-len(long_part)-j)
            
        is_impossible = sum([(int(tmp_short[k])+int(tmp_long[k]))//4 for k in range(length)])
        if not is_impossible: do_more = 0

# 옆으로 삐져 나오는 경우
while length <= len(short_part) + len(long_part) and do_more:
    length += 1
    overlapped = len(short_part) + len(long_part) - length 
    # case 1 : 짧은 배열의 뒷 부분과 긴 배열의 앞부분이 겹치는 경우
    tmp_short = short_part[-overlapped:]
    tmp_long = long_part[:overlapped]
    is_impossible = sum([(int(tmp_short[k])+int(tmp_long[k]))//4 for k in range(overlapped)])
    if not is_impossible: 
        do_more = 0
        continue
    # case 2 : 짧은 배열의 앞 부분과 긴 배열의 뒷 부분이 겹치는 경우
    tmp_short = short_part[:overlapped]
    tmp_long = long_part[-overlapped:]
    is_impossible = sum([(int(tmp_short[k])+int(tmp_long[k]))//4 for k in range(overlapped)])
    if not is_impossible: do_more = 0

print(length)
