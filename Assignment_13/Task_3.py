# This program gets a string and return reversed version of if
# The problem is solved by recursive function.
# The program also includes 2 examples to demonstrate
# working of reverse_text function.

def reverse_text(text):
    if len(text) <= 1:
        return text
    else:
        return reverse_text(text[1:]) + text[0]


def main():
    text = str(input("Enter text: "))
    reversed_text = reverse_text(text)

    print(f"The reversed text of '{text}' is '{reversed_text}'")

    # The examples that demonstrate the working of reverse_text function.
    example_1 = "Wonder Woman"  # Output: 'namoW rednoW'
    example_2 = "Figure 01"  # Output: '10 erugiF'

    reversed_example_1 = reverse_text(example_1)
    reversed_example_2 = reverse_text(example_2)

    print(f"Example #1: the reversed text of '{example_1}' is '{reversed_example_1}'")
    print(f"Example #2: the reversed text of '{example_2}' is '{reversed_example_2}'")


if __name__ == "__main__":
    main()
