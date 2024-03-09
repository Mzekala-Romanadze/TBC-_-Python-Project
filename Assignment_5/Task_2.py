# This program prints multiplication table from 1 to 9.
# The program is written in columns for each number
# and does not repeat the same multiplication from previous columns.

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > i**2:
            break
        print(f"{j} * {i} = {result}", end="  ")
    print()
