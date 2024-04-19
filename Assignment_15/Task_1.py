# This program generates 100 random numbers in range 10-1 000 000 000.
# The program finds the shortest and longest numbers in a sequence
# and order all numbers from shortest to highest and vice versa.
# Problem is solved by using min, max and sorted functions.

import random


def generate_random_numbers(quantity, min_number, max_number):
    random_numbers = []
    for _ in range(quantity):
        number = random.randint(min_number, max_number)
        random_numbers.append(number)
    return random_numbers


def main():
    min_number = 10
    max_number = 1000000000
    quantity = 100

    random_numbers = generate_random_numbers(quantity, min_number, max_number)

    shortest = min(random_numbers, key=lambda x: len(str(x)))
    longest = max(random_numbers, key=lambda x: len(str(x)))

    sorted_shortest_to_longest = sorted(random_numbers, key=lambda x: len(str(x)))
    sorted_longest_to_shortest = sorted(random_numbers, key=lambda x: len(str(x)), reverse=True)

    print("The shortest number is ", shortest)
    print("The longest number is ", longest)
    print("Sorted from shortest to longest: ", sorted_shortest_to_longest)
    print("Sorted from longest to shortest: ", sorted_longest_to_shortest)


if __name__ == "__main__":
    main()
