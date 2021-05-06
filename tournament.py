import main_file



# PRINT STATUS:
# 0 is nothing. Just Tournament stats
# 1 is End Game and lists
# 2 is every move
print_status = 2
player_1_type = "Random"
player_2_type = "Random"
number_of_games = 10

player_1_wins = 0
player_2_wins = 0
player_draws = 0

i = 0
while i < number_of_games:
    G = main_file.Game(player_1_type, player_2_type, print_status)
    result = G.play_game()
    i += 1

    if result[0] == 1:
        player_1_wins += 1
    if result[0] == 2:
        player_2_wins += 1
    if result[0] == 3:
        player_draws += 1

print("Total Games: " + str(number_of_games))
print("Player 1 Win Ratio: " + str(round((player_1_wins/i * 100), 1)))
print("Player 2 Win Ratio: " + str(round((player_2_wins/i * 100), 1)))
print("Number of Draws: " + str(player_draws))
