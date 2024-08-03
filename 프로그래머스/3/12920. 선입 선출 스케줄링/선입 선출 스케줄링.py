def solution(n, cores):
    if len(cores) >= n:
        return n
    
    left, right = 1, n * max(cores) 
    
    n -= len(cores) # 처음엔 모두 작업 바로 들어감
    while left < right:
        mid = (left + right) // 2
        done = sum([mid // core for core in cores])
        if done >= n:
            right = mid
        else:
            left = mid + 1
            
    n -= sum([(right-1) // core for core in cores]) 
    for idx, core in enumerate(cores):
        if right % core == 0: n -= 1
        if n == 0: return idx + 1
