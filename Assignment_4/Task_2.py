# This program gets a positive integer from the user
# and randomly generates integer(s) from the range 0-1000
# as many as the number the user input.
# The program prints the maximum number from them.

import random

quantity = int(input("How many integers do you want to generate? (Choose number from 1 to 30) "))


def get_integer():
    number = []
    for i in range(quantity):
        n = random.randint(0, 1000)
        number.append(n)
    return number


if quantity <= 0 or quantity > 30:
    print("Enter positive integer in range 0-30.")
else:
    result = get_integer()
    print(result)
    print(max(result))
