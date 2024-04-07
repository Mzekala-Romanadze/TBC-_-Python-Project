# This program gets an integer from the user
# and checks if it is prime number.
# The program also includes 2 examples to demonstrate
# working of check_number function.


def check_number(a):
    divisors = 0
    i = 0
    while i < a + 1:
        i += 1
        if a % i == 0:
            divisors += 1
    if divisors > 2:
        return None
    else:
        return a


def main():
    a = int(input("Enter a positive integer: "))
    if a == 1:
        print("1 is not prime number")
    elif a < 2:
        print("Please, enter positive integer. ")
    else:
        checked_num = check_number(a)
        if checked_num is not None:
            print(f"The number {a} is prime number")
        else:
            print(f"The number {a} is not prime number")

        # The examples that demonstrate the working of check_number function.
        example_1 = 11  # Prime number
        example_2 = 30  # Not prime number

        checked_example_1 = check_number(example_1)
        checked_example_2 = check_number(example_2)

        if checked_example_1 is not None:
            print(f"Example #1: the number {example_1} is prime number")
        else:
            print(f"Example #1: the number {example_1} is not prime number")

        if checked_example_2 is not None:
            print(f"Example #2: the number {example_2} is prime number")
        else:
            print(f"Example #2: the number {example_2} is not prime number")


if __name__ == "__main__":
    main()
