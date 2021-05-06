import random
import sqlite3

class Board():
    def __init__(self):
        self.player_1_set = set()
        self.player_2_set = set()
        self.move_list = []
        self.turn_count = 0
        self.create_win_conditions()
        self.possible_move_list = [1, 2, 3, 4, 5, 6, 7]

    def print_board(self):
        i = 36
        print("")
        while i > 0:
            if i in self.player_1_set:
                print('X', end="")
            elif i in self.player_2_set:
                print('O', end="")
            else:
                print('.', end ="")
            if i % 7 == 0 and i != 36:
                print("")
                i -= 14
            i += 1
        print("")

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

    def check_win(self, player_set):
        conn = sqlite3.connect('win_combo_db.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM win_conditions_table''')
        all_sets = cursor.fetchall()

        for set in all_sets:
            if all(item in player_set for item in set):
                return 1
        return 0

    def board_move(self, move, player_ID):
        print("Debugging here: ")
        print(self.possible_move_list)
        print(move)

        self.possible_move_list.remove(move)
        if move + 7 <= 42:
            self.possible_move_list.append(move+7)

        if player_ID == 1:
            self.player_1_set.add(int(move))
        if player_ID == 2:
            self.player_2_set.add(int(move))

        self.move_list.append(int(move))
        self.turn_count += 1

    # def take_back(self, move, player_ID):
    #     last_move = self.move_list[-1]
    #
    #     if player_ID == 1:
    #         self.player_1_set.remove(last_move)
    #     if player_ID == 2:
    #         self.player_2_set.remove(last_move)
    #     del self.move_list[-1]
    #     self.turn_count -= 1
    #
    #     self.possible_move_list.append(move)
    #
    #
    #     self.possible_move_list.remove(move+7)

class Player():
    def __init__(self, player_type, player_ID):
        self.player_type = player_type
        self.player_ID = player_ID

    def make_move(self, current_B):
        if self.player_type == 'Random':
            user_move = random.choice(current_B.possible_move_list)
            return user_move

        if self.player_type == 'Human':
            user_move = int(input("Human Move: "))
            return user_move

        if self.player_type == 'Stockfish':
            temp_B = Board()
            temp_B.player_1_set = current_B.player_1_set.copy()
            temp_B.player_2_set = current_B.player_2_set.copy()
            temp_B.move_list = current_B.move_list.copy()
            temp_B.turn_count = current_B.turn_count
            temp_B.possible_move_list = current_B.possible_move_list.copy()

            if self.player_ID == 1:
                current_set = temp_B.player_1_set
            if self.player_ID == 2:
                current_set = temp_B.player_2_set

            for move in temp_B.possible_move_list:
                current_set.add(move)
                print("Trying move: " + str(move))

                if current_B.check_win(current_set):
                    return move
                current_set.remove(move)
                #
                #
                # temp_B.board_move(move, self.player_ID)
                # if temp_B.check_win(set):
                #     return move
                # # temp_B.print_board()
                # temp_B.take_back(move, self.player_ID)

            user_move = random.choice(current_B.possible_move_list)

            return user_move


class Game():
    def __init__(self):
        self.B = Board()
        self.P1 = Player('Random', 1)
        self.P2 = Player('Stockfish', 2)

    def play_game(self, print_status):
        while self.B.turn_count <= 42:
            if self.B.turn_count % 2:
                current_player = self.P2
                current_set = self.B.player_2_set
            else:
                current_player = self.P1
                current_set = self.B.player_1_set

            if print_status == 2:
                self.B.print_board()

            user_move = current_player.make_move(self.B)
            self.B.board_move(user_move, current_player.player_ID)

            if self.B.check_win(current_set):
                game_result = current_player.player_ID
                if print_status:
                    self.B.print_board()
                    print(game_result, self.B.player_1_set, self.B.player_2_set)

                return (game_result, self.B.player_1_set, self.B.player_2_set)

        game_result == 3
        return (game_result, self.B.player_1_set, self.B.player_2_set)
