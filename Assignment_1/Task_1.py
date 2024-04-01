# This program gets answers from the user
# and prints user's full name and age.

name = str(input("What is your first name? "))
surname = str(input("What is your last name? "))
age = int(input("How old are you? "))

if age <= 0:
    print("Enter positive number for your age")
else:
    print("Hello, ", name, surname)
    print("You're ", age, "years old.")
