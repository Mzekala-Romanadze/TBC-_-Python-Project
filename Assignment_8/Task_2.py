# This program gets a string from the user
# and print only consonants existing in the input text.

CONSONANTS = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

user_input = str(input("Enter text: "))

text_output = ""
for c in range(len(user_input)):
    if user_input[c] in CONSONANTS:
        text_output += user_input[c]

print(text_output)
