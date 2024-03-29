# This program encrypts and decrypts the text the user has input
# and prints the result on the screen.
# The encryption algorithm is the following:
# 1. each character transforms into another character
# which is right to it on the Keyboard.
# 2. If on the right there is not any English letter
# on the keyboard, then it should move to the first character
# on the same row.
# The program only transforms lowercase English letters (a-z).

ROW_1_LETTERS = "qwertyuiop"
ROW_2_LETTERS = "asdfghjkl"
ROW_3_LETTERS = "zxcvbnm"
KEY = 1

action = input("Enter action: Encryption or Decryption (e/d)? ")
user_input = input("Please, enter text: ")

if action == "e":
    output_text = ""
    for c in user_input:
        if c in ROW_1_LETTERS:
            c_index = ROW_1_LETTERS.index(c)
            output_index = (c_index + KEY) % len(ROW_1_LETTERS)
            output_text += ROW_1_LETTERS[output_index]
        elif c in ROW_2_LETTERS:
            c_index = ROW_2_LETTERS.index(c)
            output_index = (c_index + KEY) % len(ROW_2_LETTERS)
            output_text += ROW_2_LETTERS[output_index]
        elif c in ROW_3_LETTERS:
            c_index = ROW_3_LETTERS.index(c)
            output_index = (c_index + KEY) % len(ROW_3_LETTERS)
            output_text += ROW_3_LETTERS[output_index]
        else:
            output_text += c

    print("Encrypted text is:", output_text)
elif action == "d":
    output_text = ""
    for c in user_input:
        if c in ROW_1_LETTERS:
            c_index = ROW_1_LETTERS.index(c)
            output_index = (c_index - KEY) % len(ROW_1_LETTERS)
            output_text += ROW_1_LETTERS[output_index]
        elif c in ROW_2_LETTERS:
            c_index = ROW_2_LETTERS.index(c)
            output_index = (c_index - KEY) % len(ROW_2_LETTERS)
            output_text += ROW_2_LETTERS[output_index]
        elif c in ROW_3_LETTERS:
            c_index = ROW_3_LETTERS.index(c)
            output_index = (c_index - KEY) % len(ROW_3_LETTERS)
            output_text += ROW_3_LETTERS[output_index]
        else:
            output_text += c

    print("Decrypted text is:", output_text)
else:
    print("Incorrect action")
