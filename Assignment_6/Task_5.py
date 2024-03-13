# This program gets an integer n in range 0-10 from the user
# and prints a structure for n like the following example for n=5
"""
     0
    101
   21012
  3210123
 432101234
54321012345
"""
# The problem is solved by using While loop.

n = int(input("Enter a positive integer in range 0-10: "))

if 0 < n < 10:
    i = 0
    while i <= n:
        print(" " * (n - i), end="")
        j = i
        while j >= 0:
            print(j, end="")
            j -= 1
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()
        i += 1
else:
    print("Please enter a positive integer in range 0-10")
