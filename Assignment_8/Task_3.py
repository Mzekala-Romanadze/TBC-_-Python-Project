# This program gets a string from the user
# and prints first, middle and last letter 5 times
# While loop is used to solve the problem.
# If the length of the text is even the program prints middle 2 characters.

user_input = str(input("Please, enter text: "))

first_letter = ""
middle_letter = ""
last_letter = ""

c = 0
while c < len(user_input):
    # print(user_input[c], end="")
    if c == 0:
        first_letter += user_input[c]

    if c == len(user_input) - 1:
        last_letter += user_input[c]

    if len(user_input) % 2 == 0:
        if c == len(user_input) // 2 - 1:
            middle_letter += user_input[c]
        if c == len(user_input) // 2:
            middle_letter += user_input[c]

    if len(user_input) % 2 > 0 and c == len(user_input) // 2:
        middle_letter += user_input[c]
    c += 1

print(5 * first_letter, 5 * middle_letter, 5 * last_letter)
