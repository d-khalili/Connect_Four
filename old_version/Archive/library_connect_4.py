# Connect 4 Game!
import random

# CLASS BOARD ------------------------------------

# Making the board dictionary
board_dict = {1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:".", 8:".", 9:".", 10:".", 11:".", 12:".", 13:".", 14:".", 15:".", 16:".", 17:".", 18:".", 19:".", 20:".", 21:".", 22:".", 23:".", 24:".", 25:".", 26:".", 27:".", 28:".", 29:".", 30:".", 31:".", 32:".", 33:".", 34:".", 35:".", 36:".", 37:".", 38:".", 39:".", 40:".", 41:".", 42:"."}

# Printing the Board
def print_board():
    i = 1
    k= 35
    while k > -1:
        while i < 8:
            # print(str(i+k), end=" ")
            print(board_dict[i + k], end=" ")
            i+=1
        else: print("")
        i = 1
        k -= 7

# Class PLAYER ---------------------------------------------
# Make a move
move_list = []

def make_move_human():
    user_move = int(input("Enter move: "))
    while board_dict[user_move] != '.':
        user_move += 7
    while test_move(user_move) is False:
        user_move = int(input("That move is unsupported. Please enter another move: "))

    return user_move

def make_move_random():
    user_move = random.randint(1,7)
    while board_dict[user_move] != '.':
        user_move += 7
        while test_move(user_move) is False:
            user_move = random.randint(1,8)

    return user_move

def test_move(user_move):
    if user_move <= 42:
        return True
    else:
        return False


# Class GAME ----------------------------------------------------------

# def play_game():
#     while is_game_win() is False:
def is_win():
    i = 0
    player_1_move_list = []
    player_2_move_list = []
    for move in move_list:
        if i % 2: player_2_move_list.append(move)
        else: player_1_move_list.append(move)
        i += 1
    print("Player 1 list:")
    print(player_1_move_list)


    # Horizontal checking
    x = 1
    # for m in range(6):
    for p in range (4):
        if x in player_1_move_list and x + 1 in player_1_move_list and x + 2 in player_1_move_list and x + 3 in player_1_move_list:
            print("This might be a winner?")
        x += 1
        # x += 4

for i in range(20):
    user_move = make_move_random()
    board_dict[user_move] = 'X'
    move_list.append(user_move)
    user_move = make_move_random()
    board_dict[user_move] = 'O'
    move_list.append(user_move)
    is_win()
    print_board()
    print(move_list)
