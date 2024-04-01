# This program gets two strings and
# checks if it is possible to make first string
# using symbols of second string and vice versa.
# This program works only on English letters.

SYMBOLS = "abcdefghijklmnopqrstuvwxyz "

text_1 = input("Enter first text: ").lower()
text_2 = input("Enter second text: ").lower()

first_text = ""
for c in text_1:
    if c in SYMBOLS:
        first_text += c

second_text = ""
for c in text_2:
    if c in SYMBOLS:
        second_text += c

if len(first_text) == len(second_text):
    if sorted(first_text) == sorted(second_text):
        print("Yes, it is possible.")
    else:
        print("No, it is not possible.")
else:
    print("No, it is not possible.")
