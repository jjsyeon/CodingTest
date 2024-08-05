def solution(keymap, targets):
    answer = []
    key_dict = dict()
    for key in keymap:
        for idx, alphabet in enumerate(key):
            if alphabet in key_dict:
                key_dict[alphabet] = min(key_dict[alphabet], idx +1)
            else: key_dict[alphabet] = idx+1
    for target in targets:
        temp_answer = 0
        for t in target:
            if t in key_dict.keys(): temp_answer += key_dict[t]
            else : 
                temp_answer = -1
                break
        answer.append(temp_answer)
    return answer