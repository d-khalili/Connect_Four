import random
import sqlite3

class Game():
    def __init__(self, player_1_type, playey_2_type):
        self.player_1_type = player_1
        self.player_2_type = player_2
        self.print_status = print_status
        self.board = {[],[]}
        self.possible_move_list = [1, 2, 3, 4, 5, 6, 7]
        self.move_number = 0
        self.is_win = False

    def play_game(self):
        while self.is_win is False:
            current_player_list = self.board[move_number % 2]
            move = make_move(self.board, self.possible_move_list)
            current_player_list.append(move)
            possible_move_list.remove(move)
            if move + 7 >= 42:
                possible_move_list.append(move + 7)

            is_win = is_win(current_player_list)

            if is_win True:
                return board, is_win
        return is_win, board

    def make_move(self):
        if self.player_type == 'Random':
            user_move = make_move_random()
            return user_move

    def make_move_random():
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
