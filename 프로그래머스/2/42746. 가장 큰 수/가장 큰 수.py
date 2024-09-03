def solution(numbers):
    converse = [str(n)[::-1] for n in numbers]
    converse.sort()
    answer = ''.join(converse)[::-1]
    print(converse)
    # [1000, 111, 110, 101, 100, 11, 10, 1, 0]
    # [1, 11, 111, 110, 101, 10, 100, 1000, 0]
    # 결과 1/11/1110111101010010000
    # 기대 1/11/111/110/101/10/100/1000/0
    return answer