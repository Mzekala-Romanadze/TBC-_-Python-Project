# This program gets string from the user
# and prints all characters which has even index
# except "e" character

user_input = str(input("Enter text: "))

even_index = ""
for c in range(len(user_input)):
    if c % 2 == 0 and "e" != user_input[c]:
        even_index += user_input[c]

print(even_index)
