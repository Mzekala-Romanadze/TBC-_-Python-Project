# This program generate 100 random numbers (in range -10000-10000)
# and make dictionary including 2 keys: 'even' and 'odd' -
# the value of the keys are the number of generated numbers.
# In particular, value of key 'even' is the number of even numbers from
# randomly generated numbers and value of key 'odd' is the number of odd numbers.

import random


def generate_random_numbers():
    random_numbers = []
    for _ in range(10):
        random_number = random.randint(-10000, 10000)
        random_numbers.append(random_number)
    return random_numbers


def create_dictionary(random_numbers):
    even_odd_nums_dict = {"Even": 0, "Odd": 0}

    for number in random_numbers:
        if number % 2 == 0:
            even_odd_nums_dict["Even"] += 1
        else:
            even_odd_nums_dict["Odd"] += 1

    return even_odd_nums_dict


def main():
    random_numbers = generate_random_numbers()
    generated_dictionary = create_dictionary(random_numbers)

    print("Randomly generated numbers: ", random_numbers)
    print("Even numbers: ", generated_dictionary["Even"])
    print("Odd numbers: ", generated_dictionary["Odd"])


if __name__ == "__main__":
    main()
