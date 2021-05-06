import random
import sqlite3

class Board():
    def __init__(self):
        self.move_list = []
        self.player_1_set = set()
        self.player_2_set = set()
        self.turn_count = 0
        self.win_conditions = self.create_win_conditions()
        self.possible_move_list = [1, 2, 3, 4, 5, 6, 7]

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
                return 1, set

        if self.turn_count > 41:
            return 3, {}
        # Continue otherwise
        else:
            return 0, {}

    def board_move(self, move, player_ID):
        # Checks to make sure move hasn't been won yet and then goes larger
        print("MOVE: " + str(move))
        while move in self.move_list:
            move += 7
            if move > 42:
                return 0

        while move - 7 not in self.move_list and move > 7:
            move -= 7

        if player_ID == 1:
            self.player_1_set.add(int(move))
        if player_ID == 2:
            self.player_2_set.add(int(move))

        self.move_list.append(int(move))
        self.turn_count += 1

        next_potential_move = move + 7
        self.possible_move_list.append(int(next_potential_move))
        self.possible_move_list.remove(move)

        print('Turn count: ' + str(self.turn_count))
        print('Move list: ' + str(self.move_list))
        print('Player 1 Set: ' + str(self.player_1_set))
        print('Player 2 Set: ' + str(self.player_2_set))
        print('')


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



class Game():
    def __init__(self):
        self.B = Board()
        self.P1 = Player('Human', 1)
        self.P2 = Player('Random', 2)

    def play_game(self):
        user_move = self.P1.make_move()
        while self.B.board_move(user_move, self.P1.player_ID) == 0:
            user_move = self.P1.make_move()

        if self.B.check_win(self.P1.player_ID)[0] != 0:
            print("Recording a PLAYER-1 win in play_game")
            return self.B.check_win(self.P1.player_ID)

        user_move = self.P2.make_move()
        while self.B.board_move(user_move, self.P2.player_ID) == 0:
            user_move = self.P2.make_move()

        if self.B.check_win(self.P2.player_ID)[0] != 0:
            print("Recording a PLAYER-2 win in play_game")
            return self.B.check_win(self.P2.player_ID)
