def solution(board):
    board_str = "".join(board)

    def win_case(mark):
        point = [0,0,0]
        # 가로, 세로 점수 조사
        for i in range(3):
            if board[i] == mark * 3 : point[0] += 1 # 가로 조사
            if "".join([item[i] for item in board]) == mark * 3 : point[1] += 1 # 세로 조사
        # 대각선 점수 조사
        if "".join(board[i][i] for i in range(3)) == mark * 3 : point[2] += 1
        if "".join(board[i][2-i] for i in range(3)) == mark * 3 : point[2] += 1
        
        if sum(point) == 0: return 0
        # elif point[0] > 1 or point[1] > 1: return -1
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