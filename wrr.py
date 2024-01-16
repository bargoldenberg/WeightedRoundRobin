def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    num_of_players  = len(valuations)
    num_of_items = len(valuations[0])
    players_dict = {}
    ans = []
    '''initialization'''
    for i in range(num_of_players):
        players_dict[i] = 0
    while num_of_items != 0:
        max_value = -float('inf')
        max_player = -1
        for i in range(num_of_players):
            f = players_dict[i] + y
            value = 0
            if f == 0:
                value = float('inf')
            else:
                value = rights[i]/f
            if value > max_value:
                max_value = value
                max_player = i
        item_valuation = -float()
        chosen_item = -1
        for i in range(len(valuations[max_player])):
            player_vals = valuations[max_player]
            if player_vals[i] == None:
                continue
            if player_vals[i] > item_valuation:
                item_valuation = player_vals[i]
                chosen_item = i
        print("player", max_player + 1, "takes item", chosen_item+1,"with value",item_valuation)
        ans.append([max_player+1, chosen_item+1, item_valuation])
        players_dict[max_player]+=1
        num_of_items=num_of_items-1
        '''
        deleting item from all players valuations
        '''
        for i in range(num_of_players):
            valuations[i][chosen_item] = None
    return ans

if __name__ == '__main__':
    rights=[1,2,4]
    valuations=[[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y=0.5
    arr = weighted_round_robin(rights, valuations, y)
    assert(([[3, 5, 66], [2, 4, 55], [3, 2, 33], [1, 3, 22], [3, 1, 11]].__eq__(arr)))