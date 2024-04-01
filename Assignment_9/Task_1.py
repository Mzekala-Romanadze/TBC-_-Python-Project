# This program gets a text from the user and
# checks if the given word or sentence is palindrome.
# The program ignores spaces and other symbols in sentences
# except English letters (a-z, A-Z).
# The program also ignores letter cases.

SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

text = input("Enter text: ").lower()

user_input = ""
for i in range(len(text)):
    if text[i] in SYMBOLS:
        user_input += text[i]
    else:
        user_input += text[i].replace(text[i], "")

first = ""
last = ""
if len(user_input) % 2 > 0:
    for i in range(0, (len(user_input) // 2)):
        first += user_input[i]
    for j in range((len(user_input) // 2) + 1, len(user_input)):
        last += user_input[j]

if len(user_input) % 2 == 0:
    for i in range(0, (len(user_input) // 2)):
        first = user_input[i]
    for j in range((len(user_input) // 2), len(user_input)):
        last = user_input[j]

if first == last[::-1]:
    print("It is a palindrome text.")
else:
    print("It is not a palindrome text.")
