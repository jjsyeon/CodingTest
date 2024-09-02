def solution(array, commands):
    answer = []
    for command in commands:
        sorted_array = sorted(array[command[0]-1:command[1]])
        answer.append(sorted_array[command[2]-1])
    return answer