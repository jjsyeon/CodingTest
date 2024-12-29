from collections import Counter
import sys
input = sys.stdin.readline

word_dict = []
while (word:=input().rstrip()) != '-':
    word_dict.append(Counter(word))

while (board:=input().rstrip()) != '#':
    board = Counter(board)
    frequency = {k:0 for k in board.keys()}
    for word in word_dict:
        for k, v in word.items():
            if k not in board.keys() or v > board[k]: break
        else:
            for w in word.keys(): frequency[w] += 1

    min_, max_ = min(frequency.values()), max(frequency.values())
    print(''.join(sorted([k for k in frequency.keys() if frequency[k] == min_])), min_, end=' ')
    print(''.join(sorted([k for k in frequency.keys() if frequency[k] == max_])), max_)