from math import ceil

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_point, pickup_point = [], []
    remain_d, remain_p = 0, 0
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0: 
            count = ceil((deliveries[i] - ((cap -remain_d)%cap)) / cap)
            remain_d = (deliveries[i] - ((cap -remain_d)%cap)) % cap
            deliver_point += [i] * count

        if pickups[i] != 0: 
            count = ceil((pickups[i] - ((cap -remain_p)%cap)) / cap)
            remain_p = (pickups[i] - ((cap -remain_p)%cap)) % cap
            pickup_point += [i] * count


    if len(deliver_point) == len(pickup_point):
        for i in range(len(pickup_point)):
            answer += (max(deliver_point[i], pickup_point[i]) +1)*2
    elif len(deliver_point) < len(pickup_point):
        for i in range(len(pickup_point)):
            try:
                answer += (max(deliver_point[i], pickup_point[i])+1)*2
            except:
                answer += (pickup_point[i] +1)*2
    else:
        for i in range(len(deliver_point)):
            try:
                answer += (max(deliver_point[i], pickup_point[i])+1)*2
            except:
                answer += (deliver_point[i] +1)*2
    return answer