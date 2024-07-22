def solution(bandage, health, attacks):
    max_health = health
    current = 0
    for attack in attacks:
        t = attack[0]
        damage = attack[1]
        
        health = health + (t - current - 1) * bandage[1]
        health +=  ((t - current - 1) // bandage[0]) * bandage[2]
        if health > max_health : 
            health = max_health
            
        health  -= damage
        current = t
        if health <= 0:
            return -1
    
    return health