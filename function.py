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


# def create_a_new_game():
#     return [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

# def ask_for_input(board, player_no):
#     i, j = input("Enter two numbers, seperated by comma").split(",")
    
#     while board[int(i)][int(j)] != -1:
#         print("This position is already taken!")
#         i, j = input("Enter two numbers, seperated by comma").split(",")
        

#     board[int(i)][int(j)] = player_no - 1
#     print(board)
    
# def print_board_status(board):
#     res = "\n".join([" | ".join(["O" if val == 1 else "X" if val == 0 else " " for val in row]) for row in board])
#     print(res)

# def is_player_won(player_no, board):
#     # horizontal
#     for row in board:
#         if row == [player_no - 1 for i in range(3)]:
#             return True

#     # vertical
    
#     for column_no in range(3):
#         column = []
#         for row_no in range(3):
#             column.append(board[row_no][column_no])
        
#         if column == [player_no - 1 for i in range(3)]:
#             return True
    

#     # diagonal
#     primary_diagonal = []
#     secondary_diagonal = []
#     for i in range(3):
#         primary_diagonal.append(board[i][i])
#         secondary_diagonal.append(board[i][2 - i])

#     if primary_diagonal == [player_no - 1 for i in range(3)]:
#         return True

#     if secondary_diagonal == [player_no - 1 for i in range(3)]:
#         return True

#     return False

# # def print_board_status(board):
# #     for row in board:
# #         row_string = "|"
# #         for item in row:
# #             if item == -1:
# #                 row_string += " "
# #             elif item == 0:
# #                 row_string += "O"
# #             else:
# #                 row_string += "X"

# #             row_string += "|"
        
# #         print(row_string)

# board = []

# # [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
# # -1 = empty cell
# # 0 = player 1's sign
# # 1 = player 2's sign

# board = create_a_new_game()
# # print_board_status(board)
# NO_OF_INPUTS = 9
# player_no = 1 #player 1 starts first

# for round in range(NO_OF_INPUTS):
#     print_board_status(board)
#     ask_for_input(board, player_no)

#     if player_no == 1:
#         player_no = 2
#     else:
#         player_no = 1

#     if is_player_won(1, board) == True:
#         print("player 1 has won") 
#         break
#     elif is_player_won(2, board) == True:
#         print("player 2 has won")
#         break
    
#  |  | 
#  |  |
#  |  |


# X | O | X
# O | X | O
# X | O | X

# task 1
# take i and j from user. Create a list (length i) of lists( length j) with user specified value
# example 2, 4
# 1 2 3 4 5 6 7 8 
# OUTPUT
# [[1, 2, 3, 4], [5, 6, 7, 8]]

# task 2
# take a list from user (basically task 1)
# add(or subtract or multiply or divide) a value to the list
# 2, 4
# 1 2 3 4 5 6 7 8 
# 5
# [[6, 7, 8, 9], [10, 11, 12, 13]]

i = int(input())
j = int(input())

output_list = []

for row_no in range(i):
    row = []
    for column_no in range(j):
        user_value = int(input())
        row.append(user_value)
    output_list.append(row)

print(output_list)

value_to_be_added = int(input())

for row in output_list:
    for i, value in enumerate(row):
        row[i] = row[i] + value_to_be_added

print(output_list)