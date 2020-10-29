# This is the board for Connect_4
import random

class Board():
    def __init__(self):
        self.board_dict = {1:'.', 2:'.', 3:'.', 4:'.', 5:'.', 6:'.', 7:'.', 8:'.', 9:'.', 10:'.', 11:'.', 12:'.', 13:'.', 14:'.', 15:'.', 16:'.', 17:'.', 18:'.', 19:'.', 20:'.', 21:'.', 22:'.', 23:'.', 24:'.', 25:'.', 26:'.', 27:'.', 28:'.', 29:'.', 30:'.', 31:'.', 32:'.', 33:'.', 34:'.', 35:'.', 36:'.', 37:'.', 38:'.', 39:'.', 40:'.', 41:'.', 42:'.'}
        self.move_list = []
        self.turn_count = 0

    def print_board(self):
        i = 36
        while i > 0:
            print(self.board_dict[i], end ="")
            if i % 7 == 0 and i != 36:
                print("")
                i -= 14
            i += 1
        print("")

    def make_move(self, user_move):
        Error = False
        end_move = ''
        user_move = int(user_move)
        player_pieces = ['X', 'O']
        for i in range(6):
            if user_move not in self.move_list:
                end_move = user_move
                break
            else:
                user_move += 7

        if user_move > 42:
            # print("Move is too high. BREAK")
            Error = True
            return Error

        self.board_dict[int(end_move)] = player_pieces[self.turn_count % 2]
        self.move_list.append(end_move)
        self.turn_count += 1
        return Error

    def check_win(self):
        game_won = False
        # A = Horizontal, B = Vertical, C = Diagonal Right, D = Diagonal Left
        win_possibilities = ["A", "B", "C", "D"]
        # Wincomb_dict Structure = [[starting moves], [add number, how many iterations on current row], [add number to get to next row, how many rows to try]]
        wincomb_dict = {'A': [[1,2,3,4], [1,4], [7,6]], 'B': [[1,8,15,22],[7,3],[1,7]], 'C': [[1,9,17,25],[1,4],[7,3]], 'D': [[4,10,16,22],[1,4],[7,3]]}
        for wp in win_possibilities:
            y = 0
            for j in range(wincomb_dict[wp][2][1]):
                x = 0
                for i in range(wincomb_dict[wp][1][1]):
                    if self.board_dict[wincomb_dict[wp][0][0]+x+y] == self.board_dict[wincomb_dict[wp][0][1]+x+y] == self.board_dict[wincomb_dict[wp][0][2]+x+y] == self.board_dict[wincomb_dict[wp][0][3]+x+y] != '.':
                        game_won = True
                        # To print cause of victory
                        # print(wp)
                        return game_won
                    x = x + wincomb_dict[wp][1][0]
                y = y + wincomb_dict[wp][2][0]
        return game_won

class Player():
    def __init__(self, player_type):
        self.player_type = player_type

    def player_move(self):
        if self.player_type == 'Random':
            user_move = random.randint(1,7)
            return user_move
        if self.player_type == 'Human':
            user_move = input("Make a move: ")

        return user_move

class Game():
    def __init__(self):
        self.b = Board()
        self.p1 = Player('Random')
        self.p2 = Player('Random')

    def print_results(self):
        print(game_status)

    def play_game(self):
        player_list = [self.p1, self.p2]
        turn_count = 0

        while len(self.b.move_list) < 42:
            user_move = player_list[turn_count % 2].player_move()
            self.b.make_move(user_move)
            turn_count += 1
            if self.b.check_win() is True:
                # self.b.print_board()
                # print("Game Won")
                # print (self.b.move_list)
                # print('.', end = "")
                return turn_count % 2
            # self.b.print_board()

class Tournament():
    def __init__(self):
        self.test = 'pass'

    def tournament(self):
        tourney_win_list = []
        num_games = 500
        for i in range(num_games):
            g = Game()
            winner = g.play_game()
            tourney_win_list.append(winner)
            i += 1
            print(i)
        total = 0
        for win in tourney_win_list:
            total = win + total
        print(total)


t = Tournament()
t.tournament()
