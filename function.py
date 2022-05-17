# def find_max(list_input):
#     max_number = list_input[0]
#     for number in list_input:
#         if number > max_number:
#             max_number = number

#     return max_number


# list_1 = [10, 30, 20, 50, 40]
# max_number = find_max(list_1)
# list_1.remove(max_number)
# second_max_number = find_max(list_1)
# print(second_max_number)


# TIkTokToe

# steps
# create a new game
# take 9 inputs
    # after each input
    # print the status of board
    # check whether player has won

def create_a_new_game():
    pass

def ask_for_input():
    pass

def print_board_status():
    pass

def is_player_won(player_no):
    pass

board = []

# [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
# -1 = empty cell
# 0 = player 1's sign
# 1 = player 2's sign

create_a_new_game()

NO_OF_INPUTS = 9

for round in range(NO_OF_INPUTS):
    print_board_status()
    ask_for_input()
    if is_player_won(1) == True:
        print("player 1 has won") 
        break
    elif is_player_won(2) == True:
        print("player 2 has won")
        break
    
