# This program randomly choose a number in range 0-100
# and the user have to guess it.
# The user has 10 tries.
# You can change the MAX_TRIES number and the program still works.

import random

MAX_TRIES = 10

number = random.randint(0, 100)
answer = int(input("What is your guess? "))

i = 1
while i < MAX_TRIES + 1:
    if answer == number:
        print("Congratulations, You are the winner!")
        break
    else:
        if i == MAX_TRIES:
            print("Game Over! Computer is the winner!", "The number was ", number)
            break
        if answer > number:
            print("Low")
            answer = int(input("Try again "))
        if answer < number:
            print("High")
            answer = int(input("Try again "))
    i += 1
