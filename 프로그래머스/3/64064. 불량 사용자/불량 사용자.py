from itertools import product

def is_candidate(u_id, b_id):
    if len(u_id) != len(b_id): return 0
    for idx in range(len(b_id)):
        if b_id[idx] != "*" and b_id[idx] != u_id[idx]: return 0
    return 1

def solution(user_id, banned_id):
    candidate_lst = []
    for b_id in banned_id:
        candidate = []
        for u_id in user_id:
            if is_candidate(u_id, b_id): candidate.append(u_id)
        candidate_lst.append(candidate) 

    pool = set()
    for case in list(product(*candidate_lst)):
        case = set(case)
        if len(case) == len(banned_id): 
            pool.add(" ".join(sorted(case)))

    return len(pool)