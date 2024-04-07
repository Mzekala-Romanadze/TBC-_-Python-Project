# This program gets a string and
# counts a number of vowels in it.
# The program also includes 2 examples to demonstrate
# working of check_vowel function.

VOWELS = "aeiou"


def check_vowel(text):
    count = 0
    for c in text:
        if c in VOWELS:
            count += 1
    return count


def main():
    text = str(input("Enter text: ")).lower()
    checked_vowel = check_vowel(text)

    print(f"The number of vowels in '{text.capitalize()}' is {checked_vowel}.")

    # The examples that demonstrate the working of check_vowel function.
    example_1 = "Wonder Woman"  # Output: 4
    example_2 = "Figure 01"  # Output: 3

    checked_example_1 = check_vowel(example_1)
    checked_example_2 = check_vowel(example_2)

    print(f"Example #1: the number of vowels in '{example_1.capitalize()}' is {checked_example_1}.")
    print(f"Example #2: the number of vowels in '{example_2.capitalize()}' is {checked_example_2}.")


if __name__ == "__main__":
    main()
