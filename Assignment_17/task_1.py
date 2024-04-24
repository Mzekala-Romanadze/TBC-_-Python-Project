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


def create_dictionary():
    even_odd_nums_dict = {"Even": 0, "Odd": 0}
    random_numbers = generate_random_numbers()
    print("Randomly generated numbers: ", random_numbers)  # For checking the result

    even_numbers = []
    even_numbers_counter = 0
    odd_numbers = []
    odd_numbers_counter = 0
    for i in random_numbers:
        if i % 2 == 0:
            even_numbers.append(i)
            even_numbers_counter += 1
        else:
            odd_numbers.append(i)
            odd_numbers_counter += 1

    print("Even numbers: ", even_numbers)  # For checking the result
    print("Odd numbers: ", odd_numbers)  # For checking the result

    even_odd_nums_dict["Even"] = even_numbers_counter
    even_odd_nums_dict["Odd"] = odd_numbers_counter

    return even_odd_nums_dict


def main():
    generated_dictionary = create_dictionary()
    print(generated_dictionary)


if __name__ == "__main__":
    main()
