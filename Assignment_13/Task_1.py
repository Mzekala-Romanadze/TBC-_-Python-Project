# This program converts Celsius to Fahrenheit and vice versa.
# The formulas are: C = (F - 32) * 5/9 and F = C * 9/5 + 32.
# The program gets the temperature from the user.
# The program also includes 2 examples to demonstrate
# working of convert_temperature function.


def convert_temperature(t, action):
    if action == "f":
        return t * 9 / 5 + 32
    elif action == "c":
        return (t - 32) * 5 / 9
    else:
        return None


def main():
    action = input("Choose action: convert C to F (f) or F to C (c)? ").lower()
    t = float(input(f"Enter temperature: "))

    converted_temp = convert_temperature(t, action)

    if converted_temp is not None:
        print(f"The temperature of {t} is {converted_temp} in {action.upper()}")

        # The examples that demonstrate the working of convert_temperature function.
        example_1 = float(36)  # In Celsius
        example_2 = float(96.8)  # In Fahrenheit

        converted_example_1 = convert_temperature(example_1, "f")
        converted_example_2 = convert_temperature(example_2, "c")

        print(f"Example #1: the temperature of {example_1} in C is {converted_example_1} in F.")
        print(f"Example #2: the temperature of {example_2} in F is {converted_example_2} in C.")
    else:
        print("Wrong action.")


if __name__ == "__main__":
    main()
