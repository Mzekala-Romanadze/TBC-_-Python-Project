# This program gets a positive integer n (n > 1) from the user
# and generates n pairs of random numbers 'a' and 'b'
# 'a' and 'b' are in range 0 < a < 1.
# if the value of variable counter satisfies the following condition:
# "math.sqrt(a ** 2 + b ** 2) <= 1" the value of counter must be increased by 1.
# The program prints "4 * counter / n" on the screen.

import random
import math

n = int(input("Enter positive integer (n > 1): "))

if n > 1:
    counter = 0
    for _ in range(n):
        a = random.random()
        b = random.random()
        # print("a = ", a, "b = ", b)  # Checking n pairs of random numbers 'a' and 'b'

        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter += 1

    result = 4 * counter / n
    print("The result is: ", result)
else:
    print("Incorrect number. Please, Enter positive number (n > 1).")

# Answer to the question: This program estimates the value of 'pi'.
# In particular, The more pairs of random numbers generated,
# the more accurate the estimation should be. When 'n' is larger,
# the estimation should approach the actual value of 'pi' (3.14) more closely.
