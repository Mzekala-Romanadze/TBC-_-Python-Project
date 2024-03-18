# This program gets a positive integer n in range 0-1000
# from the user and prints horizontally all divisors of the number.

n = int(input("Enter a positive integer in range 0-1000: "))

if 0 < n < 1000:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
else:
    print("Enter a positive integer in range 0-1000.")
