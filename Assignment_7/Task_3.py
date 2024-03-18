# This program gets a positive integer in range 0-10000
# and print the inverse number of it (ex: 123 inverse is 321)
# and the sum of its digits (ex: sum is 6).
# While loop is used to solve the problem.

n = int(input("Enter a positive integer in range 0-10000: "))

if 0 <= n < 10000:
    print("The number the user entered is:", n)
    print("The inverse number is: ", end="")
    digits_sum = 0
    while n > 0:
        digit = n % 10
        print(digit, end="")
        digits_sum += digit
        n //= 10
    print("\n" "The sum of its digits is:", digits_sum)
else:
    print("Please, enter a positive integer in range 0-10000")
