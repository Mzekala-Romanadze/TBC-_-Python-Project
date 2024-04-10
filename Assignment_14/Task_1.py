# This program calculates the arithmetic mean of temperature.

TEMPERATURE = [22, 25, 19, 23, 25, 26, 23]


def is_arithmetic_mean():
    total = 0
    for i in TEMPERATURE:
        total += i
    return total / len(TEMPERATURE)


def main():
    print(f"The arithmetic mean of {TEMPERATURE}: is {is_arithmetic_mean()}")


if __name__ == "__main__":
    main()
