def solution(board):
    board_str = "".join(board)

    def win_case(mark):
        point = {"row": [0,0,0], "col": [0,0,0], "dig": [0,0]}
        for idx, case in enumerate(board_str):
            r,c = idx // 3, idx % 3
            if case == mark:
                point["row"][r] += 1
                point["col"][c] += 1
                if r==1 and c == 1:
                    point["dig"][0] += 1
                    point["dig"][1] += 1  
                elif r == c: point["dig"][0] += 1
                elif r+c == 2 and r*c ==0: point["dig"][1] += 1  

        point["row"] = [p//3 for p in point["row"]]
        point["col"] = [p//3 for p in point["col"]]
        point["dig"] = [p//3 for p in point["dig"]]
        
        # 점수 없음
        if (sum(point["row"]) + sum(point["col"]) + sum(point["dig"])) == 0: return 0
    
        # 가로/세로/대각선 점수 중 하나만 나옴
        elif (sum(point["row"]) + sum(point["col"]) + sum(point["dig"])) == 1: return 1
            
        # 가로/세로 점수 두개 이상
        elif sum(point["row"]) > 1 or sum(point["col"]) > 1: return -1
        
        # 대각선 점수 둘일 때
        # if point["dig"] == [1,1]: 
            # if(sum(point["row"]) + sum(point["col"])) == 0 : return 1
            # if point["row"] not in [[0,0,0], [0,1,0]] or point["col"] not in [[0,0,0], [0,1,0]] :return -1
            # else : return 1
        
        # 가로/세로/대각선 점수 하나씩 나온 케이스
#         elif point["dig"] == [1,0]:
#             if [point["row"], point["col"]] in [[[1,0,0],[0,0,0]],
#                                                 [[0,0,1],[0,0,0]],
#                                                 [[0,0,0],[0,0,1]],
#                                                 [[0,0,0],[1,0,0]]]: return 1
#             else: return -1
            
#         elif point["dig"] == [0,1]:
#             if [point["row"], point["col"]] in [[[1,0,0],[0,0,0]],
#                                                 [[0,0,1],[0,0,0]],
#                                                 [[0,0,0],[0,0,1]],
#                                                 [[0,0,0],[1,0,0]]]: return 1
#             else: return -1
        
        # 가로/세로 점수 하나씩 
        return 1
    
    # 게임 시작 안됨
    if "."*9 == board_str : return 1
    
    # O or X 중 하나를 너무 많이 둠
    Ocount = board_str.count("O") 
    Xcount = board_str.count("X")
    if not 0 <= Ocount - Xcount <=1: return 0
    if Ocount <=2: return 1

    points = [win_case("O"), win_case("X")]
    if -1 in points: return 0
    if points == [0, 1] and Ocount == Xcount: return 1
    elif points == [1, 0] and Ocount > Xcount: return 1   
    elif points == [0, 0] : return 1
    
    return 0