def solution(players, callings):
    players_dic = {player:idx for idx,player in enumerate(players)}
    for call in callings:
        i = players_dic[call]
        players[i], players[i - 1] = players[i - 1], players[i]
        
        players_dic[players[i]] = i
        players_dic[players[i - 1]] = i - 1
        
    return players
        