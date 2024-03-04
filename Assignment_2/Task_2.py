# This program gets two integers from the user
# and checks if the first number is multiple of the second number.

first_number = float(input("What's the first number? "))
second_number = float(input("What's the second number? "))

is_multiple = first_number % second_number == 0
not_multiple = first_number % second_number > 0

if not_multiple:
    print("First number is not multiple of the second number.")
else:
    print("First number is multiple of the second number.")