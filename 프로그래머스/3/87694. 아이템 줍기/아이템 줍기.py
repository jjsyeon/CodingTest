from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    rectangle = [[v*2 for v in vertex] for vertex in rectangle]
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    max_idx = max([max(r) for r in rectangle])
    visited = [[0]*(max_idx+1) for _ in range(max_idx+1)]
    
    def check(x, y):
        count = 0 
        for rtg in rectangle:
            x1, y1, x2, y2 = rtg
            if x1 < x < x2 and y1 < y < y2: return 0
        
            if x == x1 and y1 <= y <= y2: count+=1
            elif x == x2 and y1 <= y <= y2: count+=1
            elif y == y1 and x1 <= x <= x2: count+=1
            elif y == y2 and x1 <= x <= x2: count+=1
            
        return 1 if count > 0 else 0
    
    def move(x, y, mx, my):
        if mx < 0 or mx > max_idx or my < 0 or my > max_idx: return 0
        mid_x, mid_y = (x+mx)/2 , (y+my)/2
        for rtg in rectangle:
            x1, y1, x2, y2 = rtg        
            if mid_x == x1 and y1 <= mid_y <= y2: return 1
            elif mid_x == x2 and y1 <= mid_y <= y2: return 1
            elif mid_y == y1 and x1 <= mid_x <= x2: return 1
            elif mid_y == y2 and x1 <= mid_x <= x2: return 1
            
        return 0
    
    queue = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = 1
    
    while queue:
        x, y, distance = queue.popleft()
        if x == itemX and y == itemY: return distance//2
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if not move(x,y,mx,my): continue
            if check(mx, my) and visited[mx][my] == 0:
                queue.append((mx, my, distance+1))
                visited[mx][my] = 1
