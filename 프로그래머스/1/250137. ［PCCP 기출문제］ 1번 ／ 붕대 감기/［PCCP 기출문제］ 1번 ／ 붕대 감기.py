# def solution(bandage, health, attacks):
#     max_health = health
#     current = 0
#     for attack in attacks:
#         t = attack[0]
#         damage = attack[1]
        
#         health = health + (t - current - 1) * bandage[1]
#         health +=  ((t - current - 1) // bandage[0]) * bandage[2]
#         if health > max_health : 
#             health = max_health
            
#         health  -= damage
#         current = t
#         if health <= 0:
#             return -1
    
#     return health


def solution(bandage, health, attacks):
    max_health = health
    max_time = attacks[-1][0]
    conti = 0
    attack = attacks.pop(0)
    for time in range(1, max_time+1):
        if attack[0] == time:
            health -= attack[1]
            if health <= 0: return -1
            try: attack = attacks.pop(0)
            except:pass
            conti = 0
            continue
            
        conti = (conti + 1) % bandage[0]
        
        health = min(health + bandage[1] + bandage[2], max_health) if conti == 0 else min(health + bandage[1], max_health)
            
    return health
        