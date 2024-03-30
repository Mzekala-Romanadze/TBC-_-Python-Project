# This program gets a string from the user
# and rotates each character of the text from left to right
# till would not get the same string again.
# Example 1: Input:  Hello
#            Output: oHell
#                    loHel
#                    lloHe
#                    elloH
#                    Hello


def character_rotations(text):
    rotations = []
    length = len(text)
    for i in range(length + 1):
        rotated_text = text[length - i:] + text[:length - i]
        rotations.append(rotated_text)
    return rotations


def main():
    user_input = str(input("Enter text: "))
    rotations = character_rotations(user_input)
    for rotation in rotations:
        print(rotation)


if __name__ == "__main__":
    main()
