# This program gets an integer from the user from 0 to maximum 10
# and prints prime divisors of a given integer.

# number is the integer to find prime divisors of.
number = int(input("What's an integer you want to find prime divisors of? "))

if number > 10 or number <= 0:
    print("Enter valid number")
else:
    if number == 1:
        print("The prime number is 1.")
    elif number == 3:
        print("The prime number is 3.")
    elif number == 5:
        print("The prime number is 5.")
    elif number == 7:
        print("The prime number is 7.")
    elif number == 9:
        print("The prime number is 3.")
    elif number == 2 or number == 4 or number == 8:
        print("The prime number is 2.")
    elif number == 6:
        print("The prime numbers are 2, 3.")
    else:
        print("The prime numbers are 2, 5.")
