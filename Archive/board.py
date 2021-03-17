
# Takes a number, tests if it works, adds it to board, reports back if it's a win
# Error list:
# 1 = move not an int
# 2 = move not between 1 - 7
# 3 = no spot available

class Board():

    def __init__(self):
        self.board_dict = {1:'.', 2:'.', 3:'.', 4:'.', 5:'.', 6:'.', 7:'.', 8:'.', 9:'.', 10:'.', 11:'.', 12:'.', 13:'.', 14:'.', 15:'.', 16:'.', 17:'.', 18:'.', 19:'.', 20:'.', 21:'.', 22:'.', 23:'.', 24:'.', 25:'.', 26:'.', 27:'.', 28:'.', 29:'.', 30:'.', 31:'.', 32:'.', 33:'.', 34:'.', 35:'.', 36:'.', 37:'.', 38:'.', 39:'.', 40:'.', 41:'.', 42:'.'}
        self.move_list = []
        self.error = 0
        self.turn_count = 0

    def print_board(self):
        i = 36
        print("")
        while i > 0:
            print(self.board_dict[i], end ="")
            if i % 7 == 0 and i != 36:
                print("")
                i -= 14
            i += 1
        print("")

    def is_error(self, move):
        # Make sure move is an INT
        try:
            int(move)
        except:
            error = 1
            return error
        # Makes sure move is between 1-7
        if 1 > move or move > 7 :
            error = 2
            return error
        # Make sure move is still on the board
        i = 0
        while move in self.move_list:
            move += 7
            i += 1
            if i > 5:
                error = 3
                return error
            pass
        else:
            error = self.error
            return error

    def board_move(self, move, player_piece):
        move = int(move)

        while move in self.move_list:
            move += 7

        self.board_dict[move] = player_piece
        self.move_list.append(move)
        self.turn_count += 1

        return self.board_dict

    def is_win(self):
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
