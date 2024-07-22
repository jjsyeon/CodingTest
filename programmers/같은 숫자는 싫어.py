def solution(arr):
    answer = []
    before_val = -1
    for item in arr:
        if item != before_val:
            answer.append(item)
            before_val = item
    return answer
