# 16:00~
def solution(players, callings):
    rating = {player:idx for idx, player in enumerate(players)}
    for called_player in callings:
        rate = rating[called_player]
        ## 순위 사전 반영
        rating[called_player] -= 1
        rating[players[rate-1]] += 1
        ## 리스트에 반영
        players[rate], players[rate-1] = players[rate-1],players[rate]
        
    return players