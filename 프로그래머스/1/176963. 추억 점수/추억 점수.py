def solution(name, yearning, photo):
    answer = []
    for p in photo:
        result = 0
        for i in range(len(name)):
            result += p.count(name[i]) * yearning[i]
        answer.append(result)
        
    return answer