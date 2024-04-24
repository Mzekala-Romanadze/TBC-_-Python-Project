# This program gets a string from the user
# and counts a number of each symbols in the string.
# Then prints the symbol and its quantity.


def create_dictionary(user_input):
    symbol_counter_dict = {}
    for c in user_input:
        if c in symbol_counter_dict:
            symbol_counter_dict[c] += 1
        else:
            symbol_counter_dict[c] = 1
    return symbol_counter_dict


def main():
    user_input = input("Enter text: ").lower()  # lower() is added to prevent mistakes in numbers
    generated_dictionary = create_dictionary(user_input)
    for key, value in generated_dictionary.items():
        print(f"{key} _ {value}")


if __name__ == "__main__":
    main()
