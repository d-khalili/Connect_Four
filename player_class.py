import random
from board_class import Board

# takes a dictionary and decides which number to play, 1-7

class Player():
    def __init__(self, player_type, player_num):
        self.player_type = player_type
        player_piece_list = ['X', 'O']
        self.player_piece = player_piece_list[int(player_num) - 1]
        self.opposing_piece = ''
        if self.player_piece == 'X':
            self.opposing_piece = 'O'
        else: self.opposing_piece = 'X'
        self.player_num = player_num

    def make_move_master(self, board_dict):
        if self.player_type == 'Random':
            move = self.make_move_random()

        if self.player_type == 'Human':
            move = self.make_move_human(board_dict)

        if self.player_type == 'Smart1':
            move = self.make_move_smart_1(board_dict)

        if self.player_type == 'Smart2':
            move = self.make_move_smart_2(board_dict)

        return move, self.player_piece

    def make_move_random(self):
        user_move = random.randint(1,7)
        return user_move

    def make_move_human(self, board_dict):
        temp_B = Board()
        temp_B.board_dict = board_dict.copy()
        temp_B.print_board()
        user_move = input("Make move: ")
        return int(user_move)

    def make_move_smart_1(self, board_dict):
        # Just checks if next move is winning, or blocks an opposing winning move
        temp_B = Board()
        temp_B.board_dict = board_dict.copy()

        for i in range(1, 8):
            temp_B.board_move(i, self.player_piece)
            if temp_B.is_win() is True:
                return i
            else: temp_B.board_dict = board_dict.copy()

        for i in range(1,8):
            temp_B.board_move(i, self.opposing_piece)
            if temp_B.is_win() is True:
                return i
            else: temp_B.board_dict = board_dict.copy()

        user_move = random.randint(1,7)
        return user_move

    def make_move_smart_2(self, board_dict):
        # Checks if can force a win
        # print("Start of Move Analysis")
        win_count = 0
        bad_move_list = []
        good_move_list = []
        possible_move_list = []
        temp_B = Board()

        for i in range(1,8):
            if temp_B.is_error(i) == 3:
                continue
            else: possible_move_list.append(i)


        # temp_B.print_board()
        for move in possible_move_list:
            temp_B.board_dict = board_dict.copy()
            # print("Original Board: ")
            # temp_B.print_board()
            # print("TEMP MOVE FIRST LAYER: " + str(i))
            temp_B.board_move(i, self.player_piece)
            # print("Level 1 Move Board: ")
            if temp_B.is_win() is True:
                # print("Level 1 Win Found")
                return i
            win_count = 0
            for k in range(1,8):
                temp_B.board_move(k, self.opposing_piece)
                if temp_B.is_win() is True:
                    # print("This move would lead to a guaranteed loss: " + str(i))
                    # temp_B.print_board()
                    bad_move_list.append(i)
                    temp_B.take_back()
                    break
                for p in range(1,8):
                    temp_B.board_move(p, self.player_piece)
                    # print("TEMP MOVE 3: " + str(p))
                    if temp_B.is_win() is True:
                        win_count += 1
                        # print("Level 3 Win found below. Level 3 Win Count: " + str(win_count))
                        # temp_B.print_board()
                        if win_count == 7:
                            print("ABSOLUTE WIN FOUND- Aren't you a clever boy: " + str(i))
                            # Bug where move returned is off-board, because player wins regardless
                            good_move_list.append(i)
                        temp_B.take_back()
                        break

                    temp_B.take_back()
                temp_B.take_back()
            temp_B.take_back()

        # Checks first to make sure not missing an oponent has a winning move
        temp_B.board_dict = board_dict.copy()
        for i in range(1,8):
            temp_B.board_move(i, self.opposing_piece)
            if temp_B.is_win() is True:
                return i
            else: temp_B.board_dict = board_dict.copy()

        # Solves bug of constantly returning a move that is off-board
        temp_B.board_dict = board_dict.copy()
        for user_move in good_move_list:
            if temp_B.is_error(user_move) == 0:
                return user_move

        # Solves bug if no good move left
        if len(bad_move_list) >= 6:
            # print("THERE ARE NO GOOD MOVES BREAK")
            user_move = random.randint(1,7)
            return user_move


        # BUG HERE: When you get near end of game, there is only one column to move in. But it's
        # in the bad move list, so it gets trapped in the While loop below

        # If still no good move
        user_move = random.randint(1,7)
        while user_move in bad_move_list:


            print("You do get here")
            user_move = random.randint(1,7)

        # print("Random Move playing: " + str(user_move))
        return user_move
