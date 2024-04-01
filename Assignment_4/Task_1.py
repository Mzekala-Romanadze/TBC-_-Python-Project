# This program gest number of players from the user
# and generates randomly a pair of dice for each player.

import random

number_of_player = int(input("Enter player numbers: "))

if number_of_player <= 0:
    print("Enter positive number")
else:
    for i in range(number_of_player):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        print(first_dice, second_dice)
