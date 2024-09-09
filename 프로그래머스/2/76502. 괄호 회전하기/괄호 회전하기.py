


def solution(s):
    answer = 0
    
    def check_available():
        case = list(s)
        stack = []
        for c in case:
            if c in ['[', '{', '(']: 
                stack.append(c)
                continue

            if len(stack) == 0: return 0
            if (stack.pop(), c) not in [('[',']'), ('(',')'), ('{','}')]: return 0

        if len(stack) == 0: return 1
        return 0
    
    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += check_available()
    
    return answer
