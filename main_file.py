import random
import sqlite3

class Game():
    def __init__(self, player_1_type, player_2_type, print_status):
        self.player_1_type = player_1_type
        self.player_2_type = player_2_type
        self.player_1_list = []
        self.player_2_list = []
        self.print_status = print_status
        self.possible_move_list = [1, 2, 3, 4, 5, 6, 7]
        self.move_number = 0

    def play_game(self):
        is_win = 0
        while self.move_number < 43:
            if self.print_status == 2:
                G.print_board()
            move = G.make_move(self.player_1_type)
            print(move)
            G.update_player_lists(move)
            G.update_possible_move_list(move)
            is_win = G.is_win()
            if is_win is True:
                if self.print_status is True:
                    print("Winner!")
                    G.print_board()
                return self.player_1_list, self.player_2_list, is_win
            self.move_number += 1
        print("Terminated with no Winner?")

    def make_move(self, player_type):
        if player_type == 'Random':
            user_move = G.make_move_random()

        return user_move

    def update_player_lists(self, move):
        if self.move_number % 2 == 0:
            self.player_1_list.append(move)
        if self.move_number % 2 == 1:
            self.player_2_list.append(move)

    def update_possible_move_list(self, move):
        self.possible_move_list.remove(move)
        if move + 7 >= 42:
            self.possible_move_list.append(move + 7)

    def make_move_random(self):
        user_move = int(random.choice(self.possible_move_list))
        print(user_move)
        return user_move

    def is_win():
        try:
            conn = sqlite3.connect('win_combo_db.db')
        except:
            print("Seems to be no win combo dictionary")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM win_conditions_table''')
        all_sets = cursor.fetchall()

        for set in all_sets:
            if all(item in player_move_list for item in self.player_1_list):
                return 1
        return 0

    def print_board(self):
        i = 36
        print("")
        while i > 0:
            if i in self.player_1_list:
                print('X', end="")
            elif i in self.player_2_list:
                print('O', end="")
            else:
                print('.', end ="")
            if i % 7 == 0 and i != 36:
                print("")
                i -= 14
            i += 1
        print("")


G = Game("Random", "Random", 2)
G.play_game()
