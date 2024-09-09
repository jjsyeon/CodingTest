from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    weights.sort()
    for weight in weights:
        if dic[weight]:
            answer += dic[weight]
        dic[weight] += 1
        if weight % 2 == 0:
            dic[(weight//2) * 3] += 1
        if weight % 3 == 0:
            dic[(weight//3) * 4] += 1
        dic[weight * 2] += 1
    return answer