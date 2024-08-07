def solution(park, routes):
    H, W = len(park), len(park[0])
    dir_dict = {"N":[-1, 0], "E":[0,1], "S":[1,0], "W":[0,-1]}
    
    # 시작점 찾기
    pos = "".join(park).index("S")
    y, x = pos // H, pos % H
    
    # 이동하기
    for route in routes:
        direction, length = route.split()
        ny = y + dir_dict[direction][0] * int(length)
        nx = x + dir_dict[direction][1] * int(length)
        
        # 범위 밖인지 확인
        if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
        # 장애물 확인
        elif "X" in "".join([park[y+dir_dict[direction][0]*idx][x+dir_dict[direction][1]*idx] for idx in range(1,int(length)+1)]): continue
        y, x = ny, nx
        
    return [y,x]