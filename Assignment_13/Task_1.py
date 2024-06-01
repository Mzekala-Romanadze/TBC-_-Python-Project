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


def check_temperature():
    while True:
        t = input(f"Enter temperature: ")
        try:
            number = float(t)
            return number
        except ValueError:
            print("Wrong input.Enter valid temperature")


def main():
    action = input("Choose action: convert C to F (f) or F to C (c)? ").lower()
    while action != "f" and action != "c":
        action = input("Wrong action. Choose action again: convert C to F (f) or F to C (c)? ").lower()

    t = check_temperature()

    converted_temp = convert_temperature(t, action)

    if action == "c":
        input_parameter = "F"
    else:
        input_parameter = "C"

    print(f"The temperature of {t} {input_parameter.upper()} is {converted_temp} in {action.upper()}")

    # The examples that demonstrate the working of convert_temperature function.
    example_1 = float(36)  # In Celsius
    example_2 = float(96.8)  # In Fahrenheit
    example_1_action = "f"
    example_2_action = "c"

    converted_example_1 = convert_temperature(example_1, example_1_action)
    converted_example_2 = convert_temperature(example_2, example_2_action)

    print(f"Example #1: the temperature of {example_1} in C is {converted_example_1} in {example_1_action.upper()}.")
    print(f"Example #2: the temperature of {example_2} in F is {converted_example_2} in {example_2_action.upper()}.")


if __name__ == "__main__":
    main()
