import random


def play_game():
    board = {[],[]}
    possible_move_list = [1, 2, 3, 4, 5, 6, 7]
    move_number = 0
    is_win = False

    while move_number <= 42:
        current_player_list = board[move_number % 2]
        move = make_move_random(board, possible_move_list)
        current_player_list.append(move)
        possible_move_list.remove(move)
        if move + 7 >= 42:
            possible_move_list.append(move + 7)

        is_win = is_win(current_player_list)

        if is_win True:
            return board, is_win
    return board, is_win



def make_move_random(board, possible_move_list):
    if self.player_type == 'Random':
        user_move = random.choice(current_B.possible_move_list)
        return user_move

def is_win(player_move_list):
    conn = sqlite3.connect('win_combo_db.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM win_conditions_table''')
    all_sets = cursor.fetchall()

    for set in all_sets:
        if all(item in player_move_list for item in set):
            return 1
    return 0

def print_board(board):
    i = 36
    print("")
    while i > 0:
        if i in board[0]:
            print('X', end="")
        elif i in board[1]:
            print('O', end="")
        else:
            print('.', end ="")
        if i % 7 == 0 and i != 36:
            print("")
            i -= 14
        i += 1
    print("")
