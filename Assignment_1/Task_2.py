# This program counts the age of the user.

name = str(input("What is your name? "))
year = int(input("In which year were you born? "))
age = 2024 - year

if age < 0:
    print("Enter valid year")
else:
    print("Hello,", name)
    print("You're ", age, "years old.")
