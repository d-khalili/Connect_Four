import random
import sqlite3

class Board():
    def __init__(self):
        self.player_1_set = set()
        self.player_2_set = set()
        self.move_list = []
        self.turn_count = 0
        self.create_win_conditions()

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

    def check_win(self, player_ID):
        conn = sqlite3.connect('win_combo_db.db')
        cursor = conn.cursor()

        if player_ID == 1:
            c_player_set = self.player_1_set
        if player_ID == 2:
            c_player_set = self.player_2_set

        cursor.execute('''SELECT * FROM win_conditions_table''')
        all_sets = cursor.fetchall()

        for set in all_sets:
            if all(item in c_player_set for item in set):
                return int(player_ID)

        if self.turn_count == 42:
            return 3

        else:
            return 0

    def board_move(self, move, player_ID):
        while move in self.move_list:
            move += 7
            if move > 42:
                return 0

        if player_ID == 1:
            self.player_1_set.add(int(move))
        if player_ID == 2:
            self.player_2_set.add(int(move))

        self.move_list.append(int(move))
        self.turn_count += 1

class Player():
    def __init__(self, player_type, player_ID):
        self.player_type = player_type
        self.player_ID = player_ID

    def make_move(self):
        if self.player_type == 'Random':
            user_move = int(random.randint(1,7))
            return user_move

        if self.player_type == 'Human':
            user_move = int(input("Human Move: "))
            return user_move

        if self.player_type == 'Stockfish':

            return user_move


class Game():
    def __init__(self):
        self.B = Board()
        self.P1 = Player('Random', 1)
        self.P2 = Player('Random', 2)

    def play_game(self, print_status):
        while self.B.turn_count < 43:
            if self.B.turn_count % 2:
                current_player = self.P2
            else:
                current_player = self.P1

            if print_status == 2:
                G.B.print_board()

            user_move = current_player.make_move()
            self.B.board_move(user_move, current_player.player_ID)

            if self.B.check_win(current_player.player_ID):
                game_result = self.B.check_win(current_player.player_ID)

                if print_status:
                    G.B.print_board()

                print(game_result, self.B.player_1_set, self.B.player_2_set)
                return (game_result, self.B.player_1_set, self.B.player_2_set)


        print(self.B.turn_count)
        G.B.print_board()


G = Game()
G.play_game(1)
