# This program gets a positive integer from the user
# and prints horizontally all divisors of the number.


def get_positive_integer():
    while True:
        try:
            get_number = int(input("Enter a positive integer: "))
            if 0 < get_number < 1000:
                return get_number
            else:
                print("Enter a positive integer in range 0-1000.")
        except ValueError:
            print("Enter a positive integer in range 0-1000.")


def get_divisors():
    # List that contains all divisors of the number.
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


number = get_positive_integer()
divisor = get_divisors()
print(f"The divisors of {number} are: {', '.join(map(str, divisor))}")
