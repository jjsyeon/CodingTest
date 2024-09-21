def solution(numbers, target):
    global answer
    answer= 0 
    
    def dfs(idx, result):
        global answer
        if idx == len(numbers):
            if result == target: answer += 1
            return
        
        dfs(idx+1, result+numbers[idx])
        dfs(idx+1, result-numbers[idx])
    
    dfs(0,0)
    
    return answer