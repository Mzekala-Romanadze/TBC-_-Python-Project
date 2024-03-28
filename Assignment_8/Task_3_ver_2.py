# This program gets a string from the user
# and prints first, middle and last letter 5 times
# While loop is used to solve the problem.
# If the length of the text is even the program prints middle 2 characters.

user_input = str(input("Please, enter text: "))

len_is_even = False
if len(user_input) % 2 == 0:
    mid_index = len(user_input) // 2 - 1
    len_is_even = True
else:
    mid_index = len(user_input) // 2

i = 0
while i < 5:
    if len_is_even:
        print(user_input[0], user_input[mid_index] + user_input[mid_index + 1], user_input[-1])
    else:
        print(user_input[0], user_input[mid_index], user_input[-1])
    i += 1
