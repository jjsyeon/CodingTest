def time2int(time) -> int:
    h, m = map(int, time.split(":"))
    return h * 60 + m
    
def solution(plans):
    answer = []
    remains = []
    plans = [[p[0], time2int(p[1]), p[2]] for p in plans]
    plans.sort(key = lambda x: x[1])
    # print(plans,"\n----------------------")
    current = 0
    while plans or remains:
        name, start, playtime = plans.pop(0)
        # print(current, name, start, playtime)
        # print("plnas : ",plans, "\nremains : ", remains)
        playtime = int(playtime)
        space = start - current
        # print("space : " , space)
        while space > 0 and remains:
            # print(11)
            rn, rp = remains.pop(-1)
            if space >= rp:
                space -= rp
                answer.append(rn)
            else:
                rp -= space
                remains.append([rn,rp])
                break
        
        current = start
        try:
            ns = plans[0][1]
            # print("supposed end : ", current + playtime)
            if current + playtime <= ns:
                print(1, current + playtime, ns)
                answer.append(name)
                current += playtime
            else:
                # print(2, current + playtime, ns)
                remains.append([name, current + playtime - ns])
                # print(2, remains)
                current = ns
        except:
            answer.append(name)
            if remains:
                remains.reverse()
                answer += [r[0] for r in remains]
                break
                
    return answer