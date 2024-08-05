def time2int(time) -> int:
    h, m = map(int, time.split(":"))
    return h * 60 + m
    
def solution(plans):
    # 값 초기화
    answer = []
    remains = []
    current = 0
    
    # 시간 문자열 정수로 변환
    plans = [[p[0], time2int(p[1]), p[2]] for p in plans]
    plans.sort(key = lambda x: x[1])
    
    # 계획한 과제 or 남은 과제가 있는 경우
    while plans or remains:
        name, start, playtime = plans.pop(0)
        playtime = int(playtime)
        space = start - current
        # 만약 다음 과제 전에 시간이 남고 끝내지 못한 과제가 남아있는 경우
        while space > 0 and remains:
            rn, rp = remains.pop(-1)
            if space >= rp:
                space -= rp
                answer.append(rn)
            else:
                rp -= space
                remains.append([rn,rp])
                break
        
        # 계획된 과제 수행하기
        current = start
        try: # 이후 계획된 과제 있음
            ns = plans[0][1]
            if current + playtime <= ns:
                answer.append(name)
                current += playtime
            else:
                remains.append([name, current + playtime - ns])
                current = ns
        except: # 이번이 마지막으로 계획된 과제
            answer.append(name)
            if remains:
                remains.reverse()
                answer += [r[0] for r in remains]
                break
                
    return answer