def solution(n, tops):
    MOD = 10007
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[0] = 2 + tops[0]
    
    for i in range(1, n):
        left[i] = (left[i - 1] + right[i - 1]) % MOD
        right[i] = ((left[i - 1] * (1 + tops[i])) + \
                (right[i - 1] * (2 + tops[i]))) % MOD
        
    return (left[-1] + right[-1]) % MOD