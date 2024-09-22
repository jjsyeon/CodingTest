def solution(tickets):
    for t in tickets: t.append(0)
    tickets.sort(key = lambda x: x[1])
    
    temp_route = ["ICN"]
    def dfs(from_):
        for t in tickets:
            if t[0] == from_ and t[2] == 0:
                temp_route.append(t[1])
                t[2] = 1
                dfs(t[1])
                if len(temp_route) == len(tickets)+1:
                    return temp_route
                else:
                    t[2] = 0 
                    temp_route.pop()
    
    answer = dfs("ICN")
    
    return answer