import sys
input = sys.stdin.readline
word_dict = []

while True:
    word = input().rstrip()
    if word == '-': break
    word_dict.append(word)

check_list = []
while True:
    board = input().rstrip()
    if board == '#': break
    check_list.append(board)

for i in check_list:
    freq = {}
    for j in i:
        freq[j] = 0
        for k in word_dict:
            if j in k:
                available = True
                for l in k:
                    if k.count(l) > i.count(l):
                        available = False
                        break
                if available:
                    freq[j] += 1
    min_, max_ = min(freq.values()), max(freq.values())
    print(''.join(sorted([k for k,v in freq.items() if v == min_])), min_, end=' ')
    print(''.join(sorted([k for k,v in freq.items() if v == max_])), max_)