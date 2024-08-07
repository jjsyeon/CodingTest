def solution(cards):
    answer = []
    opened = [0] * len(cards)

    for idx, card in enumerate(cards):
        if opened[idx] == 1: continue

        opened[idx] = 1
        temp_answer = 1
        next_idx = card-1
        while opened[next_idx] == 0:
            opened[next_idx] = 1
            temp_answer += 1
            next_idx = cards[next_idx]-1

        if temp_answer == len(cards): return 0

        answer.append(temp_answer)
    
    answer.sort(reverse=True)
    result = 1
    for a in range(2): 
        result *= answer[a]
    return result