
#IMPLEMENTED BY: BAR GOLDENBERG

INF = float('inf')

def find_turn(num_of_players, players_dict, y, rights):
    max_value = -INF
    max_player = -1
    for i in range(num_of_players):
            f = players_dict[i] + y
            value = 0
            if f == 0:
                value = INF
            else:
                value = rights[i]/f
            if value > max_value:
                max_value = value
                max_player = i
    return max_player

def find_desired_item(max_player):
    item_valuation = -INF
    chosen_item = -1
    for i in range(len(valuations[max_player])):
        player_vals = valuations[max_player]
        if player_vals[i] == None:
            continue
        if player_vals[i] > item_valuation:
            item_valuation = player_vals[i]
            chosen_item = i
    return [chosen_item, item_valuation]

def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    num_of_players  = len(valuations)
    num_of_items = len(valuations[0])
    players_dict = {}
    ans = []

    for i in range(num_of_players):
        players_dict[i] = 0

    while num_of_items != 0:
        max_player = find_turn(num_of_players,players_dict,y,rights)
        [chosen_item, item_valuation] = find_desired_item(max_player)
        ans.append([max_player+1, chosen_item+1, item_valuation])
        players_dict[max_player]+=1
        num_of_items=num_of_items-1
        print("player", max_player + 1, "takes item", chosen_item+1,"with value",item_valuation)

        for i in range(num_of_players):
            valuations[i][chosen_item] = None
    return ans



'''
TESTS
'''
if __name__ == '__main__':
    '''
    Explanation TEST 1 (Different Rights Different Objects)
    round 1:
        player1 = 1/(0+0.5) = 2 {1 = right, 0.5 = y}
        player2 = 2/(0+0.5) = 4
        player3 = 4/(0+0.5) = 8
        player 3 takes item 5 with value 33
    round 2:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(0+0.5) = 4
        player3 = 4/(1+0.5) = 2.66666
        player 2 takes item 4 with value 55
    round 3: 
        player1 = 1/(0+0.5) = 2
        player2 = 2/(1+0.5) = 1.33333
        player3 = 4/(1+0.5) = 2.66666
        player 3 takes item 2 with value 33
    round 4: 
        player1 = 1/(0+0.5) = 2
        player2 = 2/(1+0.5) = 1.33333
        player3 = 4/(2+0.5) = 1.6
        player 1 takes item 3 with value 22
    round 5:
        player1 = 1/(1+1.5) = 0.66666
        player2 = 2/(1+0.5) = 1.33333
        player3 = 4/(2+0.5) = 1.6
        player 3 takes item 1 with value 11
    '''
    rights=[1,2,4]
    valuations=[[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y=0.5
    print("---------------------")
    print("RUNNING TEST NUMBER 1")
    print("---------------------")
    arr = weighted_round_robin(rights, valuations, y)
    assert(([[3, 5, 66], [2, 4, 55], [3, 2, 33], [1, 3, 22], [3, 1, 11]].__eq__(arr)))
    print("---------------------")
    print("TEST NUMBER 1: SUCCESS")
    print("---------------------")
    

    '''
    EXPLANATION TEST 2 (Different Rights Same Items)
    round 1:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(0+0.5) = 4
        player3 = 4/(0+0.5) = 8
        player 3 takes item 1 with value 1
    round 2:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(0+0.5) = 4
        player3 = 4/(1+0.5) = 2.66666
        player 2 takes item 2 with value 1
    round 3:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(1+0.5) = 1.33333
        player3 = 4/(1+0.5) = 2.66666
        player 3 takes item 3 with value 1
    '''
    rights=[1,2,4]
    valuations=[[1,1,1], [1,1,1], [1,1,1]]
    y=0.5
    print("RUNNING TEST NUMBER 2")
    print("---------------------")
    arr = weighted_round_robin(rights, valuations, y)
    assert([[3,1,1],[2,2,1],[3,3,1]].__eq__(arr))
    print("---------------------")
    print("TEST NUMBER 2: SUCCESS")
    print("---------------------")

    '''
    EXPLANATION TEST 3 (Same Rights Same Items)
    round 1:
        player1 = 1/0+0.5 = 2
        player2 = 1/0+0.5 = 2
        player3 = 1/0+0.5 = 2
        player 1 takes item 1 with value 1
    round 2:
        player 1 = 1/1+0.5 = 1.33333
        player 2 = 1/0+0.5 = 2
        player 3 = 1/0+0.5 = 2
        player 2 takes item 2 with value 1
    round 3:
        player 1 = 1/1+0.5 = 1.33333
        player 2 = 1/1+0.5 = 1.33333
        player 3 = 1/0+0.5 = 2
        player 3 takes item 3 with value 1
    '''
    valuations=[[1,1,1], [1,1,1], [1,1,1]]
    y=0.5
    rights=[1,1,1]
    print("RUNNING TEST NUMBER 3")
    print("---------------------")
    arr= weighted_round_robin(rights, valuations, y)
    assert([[1,1,1],[2,2,1],[3,3,1]].__eq__(arr))
    print("---------------------")
    print("TEST NUMBER 3: SUCCESS")
    print("---------------------")

    '''
    EXPLANATION TEST 4 (Same Rights Different Items)
    round 1:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(0+0.5) = 4
        player3 = 4/(0+0.5) = 8
        player 3 takes item 2 with value 3
    round 2:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(0+0.5) = 4
        player3 = 4/(1+0.5) = 2.66666
        player 2 takes item 3 with value 3
    round 3:
        player1 = 1/(0+0.5) = 2
        player2 = 2/(1+0.5) = 1.33333
        player3 = 4/(1+0.5) = 2.66666
        player 3 takes item 1 with value 1
    '''
    valuations=[[1,3,1],[2,40,3],[1,3,2]]
    rights=[1,2,4]
    y=0.5
    print("RUNNING TEST NUMBER 4")
    print("---------------------")
    arr= weighted_round_robin(rights, valuations, y)
    assert([[3,2,3],[2,3,3],[3,1,1]].__eq__(arr))
    print("---------------------")
    print("TEST NUMBER 4: SUCCESS")
    print("---------------------")
