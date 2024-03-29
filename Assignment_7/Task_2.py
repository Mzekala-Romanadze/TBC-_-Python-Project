# This program gets a positive integer in range 0-1000
# and prints a sequence of the numbers according to
# the following conditions:
# 1. if a number is even, divide this number by 2
# 2. if a number is odd, multiply this number by 3
# and plus 1 till the program gets 1.

n = int(input("Enter a positive integer in range 0-1000: "))

if 0 < n <= 1000:
    print("the sequence of the numbers for", n, "is: ", end="")
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    print(n)
else:
    print("Please, enter a positive integer in range 0-1000")
