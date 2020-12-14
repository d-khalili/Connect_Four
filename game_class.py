from player_class import Player
from board_class import Board
# takes in a number, gives out a number and player type, takes in if win and repots out a dictionary with who won the game

class Game():
    def __init__(self, player_1_type, player_2_type, print_status):
        self.player_1_type = player_1_type
        self.player_2_type = player_2_type
        self.print_status = print_status


    def play_game(self):
        P1 = Player(self.player_1_type, 1)
        P2 = Player(self.player_2_type, 2)
        B = Board()
        player_list = [P1, P2]
        turn_count = 0
        error_count = 0
        winner_id = ''

        while turn_count < 42:
            current_player = player_list[turn_count % 2]
            move, piece = current_player.make_move_master(B.board_dict)
            # print("You are here. This is move we got coming in: " + str(move))

            if B.is_error(move) != 0:
                if B.is_error(int(move)) == 1:
                    print('ERROR CODE 1 move not int!')
                    error_count += 1
                    # print('Error count: ' + str(error_count))
                    continue
                if B.is_error(int(move)) == 2:
                    print('ERROR CODE 2 move not 1-7!')
                    error_count += 1
                    # print('Error count: ' + str(error_count))
                    if current_player.player_type == 'Human':
                        continue
                    else:
                        break
                if B.is_error(int(move)) == 3:
                    # print('ERROR CODE 3 move off board')
                    error_count += 1
                    # print('Error count: ' + str(error_count))
                    continue
            error_count = 0

            B.board_move(move, piece)
            if self.print_status == 2:
                B.print_board()
            if B.is_win() is True:
                winner_id = (turn_count % 2) + 1
                print("Game Won!!!")
                break
            turn_count += 1
        if winner_id == '':
            winner_id = 3

        if self.print_status == 1 or self.print_status == 2:
            print("FINAL BOARD: ")
            B.print_board()
            print(B.board_dict)
            print('')
            print(B.move_list)

        return winner_id, B.board_dict


class Tournament():
    def __init__(self, number_games, player_1, player_2, print_status):
        self.number_games = number_games
        self.player_1 = player_1
        self.player_2 = player_2
        self.print_status = print_status

    def play_tournament(self):
        tourney_dict = {}
        tourney_dict_meta = {}
        p1_win_count = 0
        p2_win_count = 0
        draw_win_count = 0

        for i in range(self.number_games):
            Gi = Game(self.player_1, self.player_2, self.print_status)
            winner_id, board_dict = Gi.play_game()
            tourney_dict[winner_id] = board_dict
            tourney_dict_meta[i] = tourney_dict
            tourney_dict = {}

            if winner_id == 1:
                p1_win_count += 1
            if winner_id == 2:
                p2_win_count += 1
            if winner_id == 3:
                draw_win_count += 1

        # for key, value in tourney_dict_meta.items():
        #     # print('')
        #     # print (key, value)
        #     # print('')
        print('')
        print("Player 1: " + str(p1_win_count))
        print("Player 2: " + str(p2_win_count))
        print("Draws: " + str(draw_win_count))
        print('')


    def count_wins():
        pass


# Inputs: How many games, Player1 Type, Player 2 Type, Whether to print (0 = nothing, 1 = when game finished, 2 = every move)

if __name__ == '__main__':
    T = Tournament(1, "Random", 'Smart2', 1)
    T.play_tournament()
