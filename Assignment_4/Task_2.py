# This program gets a positive integer n from the user
# and randomly generates integer(s) from the range 0-1000
# as many as the number the user input.
# The program prints the highest number from them.

import random

n = int(input("How many integers do you want to generate? (Choose number from 1 to 30) "))

if 0 < n < 30:
    print("The generated numbers are: ")
    maximum = 0
    for i in range(n):
        random_number = random.randint(0, 1000)
        print(random_number)
        if random_number > maximum:
            maximum = random_number
    print("The highest number generated is:", maximum)
else:
    print("Enter positive integer in range 0-30.")
