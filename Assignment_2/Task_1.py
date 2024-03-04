# This program checks if the user's answer is either true or false.
# if the user's answer is true and prints "Whoala" if it is.

def check_answer():
    answer = int(input("What is the smallest integer divisible by 8 starting from 100? ")) == 104

    if answer is True:
        print("Whoala")
    else:
        print("Wrong")


check_answer()
