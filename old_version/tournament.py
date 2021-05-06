import game

# PRINT STATUS:
# 0 is nothing. Just Tournament STAT
# 1 is End Game plus sets
# 2 is every move
print_status = 1
number_of_games = 1000


player_1_wins = 0
player_2_wins = 0
player_draws = 0

i = 0
while i < number_of_games:
    G = game.Game()
    result = G.play_game(print_status)
    i += 1

    if result[0] == 1:
        player_1_wins += 1
    if result[0] == 2:
        player_2_wins += 1
    if result[0] == 3:
        player_draws += 1

    # print(result[0])

print("Player 1 Score: " + str(round((player_1_wins/i * 100), 1)))
print("Player 2 Score: " + str(round((player_2_wins/i * 100), 1)))
print("Number of Draws: " + str(player_draws))
