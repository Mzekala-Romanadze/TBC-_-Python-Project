# This program gets two sorted list from the user
# and returns new list in which the program sorts
# elements from both list.
# The problem is solved without using functions: sort and sorted.


def merge_lists(list_1, list_2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    while i < len(list_1):
        merged_list.append(list_1[i])
        i += 1

    while j < len(list_2):
        merged_list.append(list_2[j])
        j += 1

    return merged_list


def main():
    list_1 = []
    for x in input("Enter sorted list 1: ").split():
        list_1.append(int(x))

    list_2 = []
    for x in input("Enter sorted list 1: ").split():
        list_2.append(int(x))

    merged_list = merge_lists(list_1, list_2)

    print("The merged and sorted list: ", merged_list)


if __name__ == "__main__":
    main()
