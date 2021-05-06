import random
import sqlite3
import stockfish

class Game():
    def __init__(self, player_1_type, player_2_type, print_status):
        self.player_1_type = player_1_type
        self.player_2_type = player_2_type
        self.player_1_list = []
        self.player_2_list = []
        self.print_status = print_status
        self.possible_move_list = [1, 2, 3, 4, 5, 6, 7]
        self.move_number = 0
        self.player_lists = [self.player_1_list, self.player_2_list]
        self.player_types_list = [self.player_1_type, self.player_2_type]

    def play_game(self):
        while self.move_number < 42:
            current_player_type = self.player_types_list[self.move_number % 2]
            current_player_list = self.player_lists[self.move_number % 2]

            move = self.make_move(current_player_type)
            self.update_table(move, current_player_list)
            if self.print_status == 2:
                self.print_board()
                print("User move: " + str(move))

            if self.is_win(current_player_list) != 0:
                win_id = (self.move_number % 2) + 1
                if self.print_status != 0:
                    print("Winner is Player: " + str(win_id) + " ("+ str(current_player_type) + ")")
                    self.print_board()
                return win_id, self.player_1_list, self.player_2_list

            self.move_number += 1

        print("This is a Draw?")
        win_id = 3
        return win_id, self.player_1_list, self.player_2_list

    def make_move(self, player_type):
        if player_type == 'Random':
            user_move = self.make_move_random()
        if player_type == 'Human':
            user_move = self.make_move_human()
        if player_type == 'Stockfish':
            user_move = stockfish.make_move_stockfish()
        return user_move

    def make_move_random(self):
        user_move = int(random.choice(self.possible_move_list))
        return user_move

    def make_move_human(self):
        user_move = int(input("Human Move: "))
        return user_move

    def make_move_stockfish(self):
        pass

    def update_table(self, user_move, current_player_list):
        current_player_list.append(user_move)
        self.possible_move_list.remove(user_move)
        if user_move + 7 <= 42:
            self.possible_move_list.append(user_move + 7)

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

    def is_win(self, current_player_list):
        try:
            conn = sqlite3.connect('win_combo_db.db')
        except:
            self.create_win_conditions()
            conn = sqlite3.connect('win_combo_db.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM win_conditions_table''')
        all_win_conditions = cursor.fetchall()
        for win_set in all_win_conditions:
            if all(item in current_player_list for item in win_set):
                return 1
        return 0

    def create_win_conditions(self):
        conn = sqlite3.connect('win_combo_db.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''CREATE TABLE win_conditions_table('move_one' integer, 'move_two' integer, 'move_three' integer, 'move_four' integer)''')
            # A = Horizontal, B = Vertical, C = Diagonal Right, D = Diagonal Left
            win_possibilities = ["A", "B", "C", "D"]
            # Wincomb_dict Structure = [[starting moves], [add number, how many iterations on current row], [add number to get to next row, how many rows to try]]
            wincomb_dict = {'A': [[1,2,3,4], [1,4], [7,6]], 'B': [[1,8,15,22],[7,3],[1,7]], 'C': [[1,9,17,25],[1,4],[7,3]], 'D': [[4,10,16,22],[1,4],[7,3]]}
            for wp in win_possibilities:
                y = 0
                for j in range(wincomb_dict[wp][2][1]):
                    x = 0
                    for i in range(wincomb_dict[wp][1][1]):
                        win_list = []
                        for k in range(4):
                            win_list.append(wincomb_dict[wp][0][k]+x+y)

                        cursor.execute('''INSERT INTO win_conditions_table(move_one, move_two, move_three, move_four) VALUES (?, ?, ?, ?)''', win_list)
                        conn.commit()

                        # win_condition_list.append(win_set)
                        x = x + wincomb_dict[wp][1][0]
                    y = y + wincomb_dict[wp][2][0]
            conn.close()
        except:
            pass
