def solution(arr):
    answer = 0
    arr = ''.join(arr).split('-')
    max_val,min_val = 0,0

    for i in range(len(arr)-1, 0, -1):
        min_tmp, max_tmp = -eval(arr[i]), eval('-' + arr[i])
        max_val = max(max_val + max_tmp, -min_val + min_tmp)
        min_val = min(min_val + min_tmp, -max_val + max_tmp)
    
    answer = eval(arr[0]) + max_val        
    
    return answer