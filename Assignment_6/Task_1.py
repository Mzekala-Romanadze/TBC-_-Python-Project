# This program prints multiplication table from 1 to 9.
# The program is written in columns for each number
# and does not repeat the same multiplication from previous columns.
# The problem is solved by using While loop.

i = 1
while i < 10:
    j = 1
    while i < 10:
        result = i * j
        if result > i ** 2:
            break
        print(f"{j} * {i} = {result}", end="  ")
        j += 1
    print(" ")
    i += 1
