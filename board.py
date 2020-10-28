# This is the board for Connect_4

# class Board(object):
#     def __init__(self, player_1, player_2):
#         asdf

board_dict = {1:'.', 2:'.', 3:'.', 4:'.', 5:'.', 6:'.', 7:'.', 8:'.', 9:'.', 10:'.', 11:'.', 12:'.', 13:'.', 14:'.', 15:'.', 16:'.', 17:'.', 18:'.', 19:'.', 20:'.', 21:'.', 22:'.', 23:'.', 24:'.', 25:'.', 26:'.', 27:'.', 28:'.', 29:'.', 30:'.', 31:'.', 32:'.', 33:'.', 34:'.', 35:'.', 36:'.', 37:'.', 38:'.', 39:'.', 40:'.', 41:'.', 42:'.'}


def make_move():
    user_move = input("Make a move: ")
    board_dict[int(user_move)] = 'X'

for i in range(4):
    make_move()
print (board_dict)

def check_win():
    game_won = False

    # Horizontal Check
    y = 0
    for j in range(6):
        x = 0
        for i in range(4):
            if board_dict[1+x+y] == board_dict[2+x+y] == board_dict[3+x+y] == board_dict[4+x+y] == 'X':
                print("Game Won")
                game_won = True
                break
            x = x + 1
        y = y + 7

    # Vertical Check
    y = 0
    for j in range(7):
        x = 0
        for i in range(3):
            if board_dict[1+x+y] == board_dict[8+x+y] == board_dict[15+x+y] == board_dict[22+x+y] == 'X':
                print("Game Won")
                game_won = True
                break
            x = x + 7
        y = y + 1

check_win()
