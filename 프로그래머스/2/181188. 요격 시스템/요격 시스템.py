def solution(targets):
    answer = 0
    boundary = 0
    for s, e in sorted(targets):
        if boundary > s:
            boundary = min(boundary, e)
        else:
            boundary = e
            answer += 1

    return answer