def solution(citations):
    citations.sort(reverse=True)
    for h in range(citations[0], -1, -1):
        for idx in range(len(citations)):
            if citations[idx] < h:break
            if idx == len(citations)-1: idx = len(citations)
        if idx >= h: return h
