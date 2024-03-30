# This program gets 2 strings from the user
# and checks if the second string can be got from
# the first string's characters rotations.
# Example 1: Input a: stop
#            Input b: tops
#            Output: Yes


def character_rotations(text):
    rotations = []
    length = len(text)
    for i in range(length + 1):
        rotated_text = text[length - i:] + text[:length - i]
        rotations.append(rotated_text)
    return rotations


def check_rotation(string_a, string_b):
    rotations = character_rotations(string_a)
    return string_b in rotations


def main():
    string_a = input("Input a: ")
    string_b = input("Input b: ")

    if check_rotation(string_a, string_b):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
