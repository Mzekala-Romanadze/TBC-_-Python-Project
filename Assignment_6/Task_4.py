# This program gets an integer n in range 0-10 from the user
# and prints a structure for n like the following example for n=5
"""
1
12
123
1234
12345
1234
123
12
1
"""
# The problem is solved by using While loop.

n = int(input("Enter a positive integer in range 0-10: "))

if 0 < n < 10:
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1
    i = n - 1
    while i >= 1:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i -= 1
else:
    print("Please enter a positive integer in range 0-10")
