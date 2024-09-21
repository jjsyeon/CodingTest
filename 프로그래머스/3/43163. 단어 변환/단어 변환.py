from collections import deque

def count_differ(before, after):
    count = 0
    for i in range(len(before)):
        if before[i] != after[i]: count+=1
        if count > 1: return 0
    return 1 if count == 1 else 0
        

def solution(begin, target, words):
    if target not in words: return 0
    
    visited = [0] * len(words)
    
    queue = deque([(begin,0)])
    while queue:
        before, answer = queue.popleft()
        for idx, after in enumerate(words):
            if visited[idx]: continue
            if count_differ(before, after):
                visited[idx] = 1
                if after == target: return answer+1
                queue.append((after, answer+1))
    return 0