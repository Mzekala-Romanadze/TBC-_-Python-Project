# This program gets two strings and
# checks if it is possible to make first string
# using symbols of second string and vice versa.
# This program works only on English letters.

SYMBOLS = "abcdefghijklmnopqrstuvwxyz "

text_1 = input("Enter first text: ").lower()
text_2 = input("Enter second text: ").lower()

first_text = ""
for i in range(len(text_1)):
    if text_1[i] in SYMBOLS:
        first_text += text_1[i]
    else:
        first_text += text_1[i].replace(text_1[i], "")

second_text = ""
for i in range(len(text_2)):
    if text_2[i] in SYMBOLS:
        second_text += text_2[i]
    else:
        second_text += text_2[i].replace(text_2[i], "")

if len(first_text) == len(second_text):
    result = 0
    for i in range(len(first_text)):
        if first_text[i] in second_text:
            result += 1
    if result == len(first_text):
        print("Yes, it is possible.")
else:
    print("No, it is not possible.")
