# This program prints multiplication table from 1 to 9.
# The program is written in columns for each number
# and does not repeat the same multiplication from previous columns.
# The problem is solved by using While loop.

x = 1
while x < 10:
    y = 1
    while y <= x:
        result = x * y
        space = "  "
        print(f"{y} * {x} = {result}{space}", end=" ")
        y += 1
    print("  ")
    x += 1
