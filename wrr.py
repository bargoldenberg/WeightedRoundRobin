#IMPLEMENTED BY: BAR GOLDENBERG
from colorama import Fore

# QUESTION 2

INF = float('inf')

def find_turn(num_of_players, players, y, rights):
    max_value = -INF
    max_player = -1
    for i in range(num_of_players):
        f = players[i] + y
        value = INF if f == 0 else rights[i]/f
        if value > max_value:
            max_value = value
            max_player = i
    return max_player

def find_desired_item(max_player):
    item_valuation = -INF
    chosen_item = -1
    for i in range(len(valuations[max_player])):
        player_vals = valuations[max_player]
        if player_vals[i] and player_vals[i] > item_valuation:
            item_valuation = player_vals[i]
            chosen_item = i
    return [chosen_item, item_valuation]

def remove_item(player_items, item_to_delete):
    player_items[item_to_delete] = None

def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    num_of_players  = len(valuations)
    num_of_items = len(valuations[0])
    players = [0 for _ in range(num_of_players)]
    ans = []
    for _ in range(num_of_items):
        chosen_player = find_turn(num_of_players,players,y,rights)
        [chosen_item, item_valuation] = find_desired_item(chosen_player)
        ans.append([chosen_player + 1, chosen_item + 1, item_valuation])
        players[chosen_player] += 1
        print("player", chosen_player + 1, "takes item", chosen_item + 1, "with value", item_valuation)
        #remove chosen item from players valuation lists.
        for i in range(num_of_players):
            remove_item(valuations[i], chosen_item)
    return ans

def run_test(rights, valuations, y, expected_out, test_number, test_name):
    print(Fore.CYAN + f"RUNNING TEST NUMBER {test_number} - ({test_name})" + Fore.WHITE)
    print("---------------------")
    arr = weighted_round_robin(rights, valuations, y)
    try:
        assert((expected_out.__eq__(arr)))
        print("---------------------")
        print(f"TEST NUMBER {test_number}: "+Fore.GREEN+"SUCCESS"+Fore.WHITE)
        print("---------------------")
    except:
        print("---------------------")
        print(f"TEST NUMBER {test_number}: "+Fore.RED+"FAILED"+Fore.WHITE)
        print("---------------------")



'''
TESTS
'''
if __name__ == '__main__':
    '''
    Explanation TEST 1 (Different Rights Different Items)
    round 1:
        player1 = 1/(0+0.5) = 2 {1 = right, 0.5 = y}
        player2 = 2/(0+0.5) = 4
        player3 = 4/(0+0.5) = 8
        player 3 takes item 5 with value 66
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
    print("---------------------")
    rights = [1,2,4]
    valuations = [[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y = 0.5
    expected_out= [[3, 5, 66], [2, 4, 55], [3, 2, 33], [1, 3, 22], [3, 1, 11]]
    run_test(rights, valuations, y, expected_out, 1 , "Different Rights Different Items")
    '''
    EXPLANATION TEST 2 (Same Rights Different Items)
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
    expected_out = [[3,2,3],[2,3,3],[3,1,1]]
    run_test(rights, valuations, y, expected_out, 2, "Same Rights Different Items")
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
    expected_out = [[1,1,1],[2,2,1],[3,3,1]]
    run_test(rights, valuations, y, expected_out, 3, "Same Rights Same Items")
    '''
    EXPLANATION TEST 4 (Different Rights Same Items)
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
    expected_out = [[3,1,1],[2,2,1],[3,3,1]]
    run_test(rights, valuations, y, expected_out, 4, "Different Rights Same Items")
    '''
    TEST NUMBER 5 (y = 0)
    '''
    rights=[1,2,4]
    valuations=[[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y=0
    expected_out = [[1,5,44],[2,4,55],[3,2,33],[3,3,22],[2,1,11]]
    run_test(rights, valuations, y, expected_out, 5, "y = 0")
    '''
    TEST NUMBER 6 (y = 1)
    '''
    rights=[1,2,4]
    valuations=[[11,11,22,33,44], [11,22,44,55,66], [11,33,22,11,66]]
    y=1
    expected_out = [[3,5,66],[2,4,55],[3,2,33],[3,3,22],[1,1,11]]
    run_test(rights, valuations, y, expected_out, 6, "y = 1")