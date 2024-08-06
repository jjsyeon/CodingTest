def solution(park, routes):
    H, W = len(park), len(park[0])
    dir_dict = {"N":[-1, 0], "E":[0,1], "S":[1,0], "W":[0,-1]}
    
    # 시작점 찾기
    pos = "".join(park).index("S")
    y, x = pos // H, pos % H
    
    # 이동하기
    for route in routes:
        direction, length = route.split()
        temp_y = y + dir_dict[direction][0] * int(length)
        temp_x = x + dir_dict[direction][1] * int(length)
        
        # 범위 밖인지 확인
        if temp_y < 0 or temp_y >= H or temp_x < 0 or temp_x >= W: continue
        # 장애물 확인
        elif "X" in "".join([park[y+dir_dict[direction][0]*idx][x+dir_dict[direction][1]*idx] for idx in range(1,int(length)+1)]):continue
        y, x = temp_y, temp_x
        
    return [y,x]