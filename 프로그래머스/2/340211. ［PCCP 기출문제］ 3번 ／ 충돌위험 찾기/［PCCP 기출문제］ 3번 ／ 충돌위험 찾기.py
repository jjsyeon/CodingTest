import copy

def solution(points, routes):
    answer = 0
    current = [points[r.pop(0) - 1]+[0] for r in routes]
    cases = copy.deepcopy(current)

    def move(idx):
        if current[idx][:2] == points[routes[idx][0]-1]:
            routes[idx].pop(0)
            return
        elif current[idx][0] != points[routes[idx][0]-1][0]:
            if current[idx][0] > points[routes[idx][0]-1][0]: 
                current[idx][0] -= 1
            else: current[idx][0] += 1
        elif current[idx][1] != points[routes[idx][0]-1][1]:
            if current[idx][1] > points[routes[idx][0]-1][1]: current[idx][1] -= 1
            else: current[idx][1] += 1
        
        current[idx][2] += 1
        cases.append(copy.deepcopy(current[idx]))
        

    def count_unique_duplicates():
        counts = {}

        for item in cases:
            item_tuple = tuple(item)
            if item_tuple in counts:
                counts[item_tuple] += 1
            else:
                counts[item_tuple] = 1

        duplicate_count = sum(1 for count in counts.values() if count > 1)

        return duplicate_count

    while sum([len(route) for route in routes]):
                        
        for idx in range(len(current)):
            if len(routes[idx]) != 0:
                move(idx)
    return count_unique_duplicates()