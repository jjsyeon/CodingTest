def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
        
    return answer