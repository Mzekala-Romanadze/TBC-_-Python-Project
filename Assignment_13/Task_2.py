# This program gets an integer from the user
# and checks if it is prime number.
# The program also includes 2 examples to demonstrate
# working of is_prime_number function.


def is_prime_number(number):
    if number == 1 or number == 0:
        print(f"Input number {number} is not prime number.")
        exit(1)

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("There are no negative prime numbers. Please, enter positive integer.")
    else:
        checked_number = is_prime_number(number)
        if checked_number:
            print(f"The number {number} is prime number")
        else:
            print(f"The number {number} is not prime number")

        # The examples that demonstrate the working of is_prime_number function.
        example_1 = 11  # Prime number
        example_2 = 30  # Not prime number

        checked_example_1 = is_prime_number(example_1)
        checked_example_2 = is_prime_number(example_2)

        if checked_example_1:
            print(f"Example #1: the number {example_1} is prime number")
        else:
            print(f"Example #1: the number {example_1} is not prime number")

        if checked_example_2:
            print(f"Example #2: the number {example_2} is prime number")
        else:
            print(f"Example #2: the number {example_2} is not prime number")


if __name__ == "__main__":
    main()
