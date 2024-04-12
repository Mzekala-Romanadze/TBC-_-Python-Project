# This program creates 3 lists with random numbers.
# The program prints the sum of the numbers having the same index.

from Task_1 import generate_random_numbers


def sum_same_index_numbers(list_1, list_2, list_3):
    max_length = max(len(list_1), len(list_2), len(list_3))
    sum_list = []
    for i in range(max_length):
        temp_sum = 0
        if i < len(list_1):
            temp_sum += list_1[i]
        if i < len(list_2):
            temp_sum += list_2[i]
        if i < len(list_3):
            temp_sum += list_3[i]
        sum_list.append(temp_sum)
    return sum_list


def main():
    list_1 = generate_random_numbers(quantity=10, min_number=1, max_number=1000)
    list_2 = generate_random_numbers(quantity=10, min_number=1, max_number=1000)
    list_3 = generate_random_numbers(quantity=10, min_number=1, max_number=1000)

    print("List 1:", list_1)
    print("List 2:", list_2)
    print("List 3:", list_3)

    sum_list = sum_same_index_numbers(list_1, list_2, list_3)
    print("The sum of the numbers at the same index in the lists:", sum_list)


if __name__ == "__main__":
    main()
