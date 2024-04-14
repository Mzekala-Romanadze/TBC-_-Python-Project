# This program generates 50 random numbers
# in range 1-30 and make a list of them.
# The program writes each element in new list as many times as its value.
# At last, the program prints the new list and length of it.

import random


def generate_list():
    original_list = []
    for _ in range(50):
        number = random.randint(1, 30)
        original_list.append(number)
    return original_list


def second_list(original_list):
    list_2 = []
    for i in original_list:
        list_2.extend([i] * i)
    return list_2


def main():
    original_list = generate_list()
    second_generated_list = second_list(original_list)

    print(f"The original list: {original_list}")
    print(f"The second generated list: {second_generated_list}")
    print(f"The length of second list: {len(second_generated_list)}")


if __name__ == "__main__":
    main()
