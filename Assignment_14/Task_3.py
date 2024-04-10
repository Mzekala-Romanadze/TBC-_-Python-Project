# This program generates 50 random numbers
# in range 1-30 and make a list of them.
# The program deletes duplicate elements in the list and
# prints the new list and length of it.

from Task_2 import generate_list


def remove_duplicates(original_list):
    unique_numbers = []
    for i in original_list:
        if i not in unique_numbers:
            unique_numbers.append(i)
    return unique_numbers


def main():
    original_list = generate_list()
    second_generated_list = remove_duplicates(original_list)

    print(f"The original list: {original_list}")
    print(f"The list after removing duplicates: {second_generated_list}")
    print(f"The length of second list: {len(second_generated_list)}")


if __name__ == "__main__":
    main()
